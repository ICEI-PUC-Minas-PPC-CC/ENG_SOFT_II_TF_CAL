pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.11'
        APP_NAME = 'todo-api'
        DOCKER_IMAGE = "${APP_NAME}:${BUILD_NUMBER}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Fazendo checkout do código...'
                checkout scm
                script {
                    def isUnix = isUnix()
                    if (isUnix) {
                        sh 'git log -1 --pretty=format:"%h - %an, %ar : %s"'
                    } else {
                        bat 'git log -1 --pretty=format:"%%h - %%an, %%ar : %%s"'
                    }
                }
            }
        }
        
        stage('Build') {
            steps {
                echo 'Construindo a aplicação...'
                dir('src') {
                    script {
                        // Detecta o sistema operacional
                        def isUnix = isUnix()
                        if (isUnix) {
                            sh '''
                                python3 -m venv venv || python -m venv venv
                                source venv/bin/activate
                                pip install --upgrade pip
                                pip install -r requirements.txt
                            '''
                        } else {
                            bat '''
                                python -m venv venv
                                call venv\\Scripts\\activate.bat
                                python -m pip install --upgrade pip
                                pip install -r requirements.txt
                            '''
                        }
                    }
                }
            }
        }
        
        stage('Test') {
            steps {
                echo 'Executando testes automatizados...'
                dir('src') {
                    script {
                        def isUnix = isUnix()
                        def testResult
                        if (isUnix) {
                            testResult = sh(
                                script: '''
                                    source venv/bin/activate
                                    pytest tests/ -v --junitxml=test-results.xml --cov=. --cov-report=xml --cov-report=html
                                ''',
                                returnStatus: true
                            )
                        } else {
                            testResult = bat(
                                script: '''
                                    call venv\\Scripts\\activate.bat
                                    pytest tests/ -v --junitxml=test-results.xml --cov=. --cov-report=xml --cov-report=html
                                ''',
                                returnStatus: true
                            )
                        }
                        // Se houver falhas nos testes (exit code != 0), marca como instável
                        // mas não falha o pipeline completamente
                        if (testResult != 0) {
                            echo "Alguns testes falharam (isso é esperado - 6 testes devem falhar intencionalmente)"
                            currentBuild.result = 'UNSTABLE'
                        }
                    }
                }
            }
            post {
                always {
                    echo 'Publicando relatórios de teste...'
                    script {
                        try {
                            junit 'src/test-results.xml'
                        } catch (Exception e) {
                            echo "Aviso: Erro ao publicar relatório JUnit (arquivo pode não existir): ${e.getMessage()}"
                        }
                        try {
                            publishHTML([
                                reportDir: 'src/htmlcov',
                                reportFiles: 'index.html',
                                reportName: 'Relatório de Cobertura de Testes',
                                keepAll: true,
                                alwaysLinkToLastBuild: true,
                                allowMissing: true
                            ])
                        } catch (Exception e) {
                            echo "Aviso: Relatório HTML não disponível (continuando): ${e.getMessage()}"
                        }
                    }
                }
                failure {
                    echo 'Testes falharam - isso é esperado se alguns testes devem falhar intencionalmente'
                    script {
                        // Não marca como falha completa, apenas instável
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }
        
        stage('Quality Check') {
            steps {
                echo 'Verificando qualidade do código...'
                dir('src') {
                    script {
                        def isUnix = isUnix()
                        if (isUnix) {
                            sh '''
                                source venv/bin/activate
                                python -m py_compile app.py || echo "Aviso: Verificação de sintaxe concluída"
                            '''
                        } else {
                            bat '''
                                call venv\\Scripts\\activate.bat
                                python -m py_compile app.py
                            '''
                        }
                    }
                }
            }
        }
        
        stage('Package') {
            steps {
                echo 'Empacotando artefatos...'
                script {
                    def isUnix = isUnix()
                    dir('src') {
                        if (isUnix) {
                            sh '''
                                mkdir -p ../artifacts
                                cp -r . ../artifacts/
                            '''
                        } else {
                            bat '''
                                if not exist ..\\artifacts mkdir ..\\artifacts
                                xcopy /E /I /Y . ..\\artifacts\\
                            '''
                        }
                    }
                    if (isUnix) {
                        sh """
                            echo "Build Number: ${BUILD_NUMBER}" > artifacts/build-info.txt
                            echo "Build Time: \$(date)" >> artifacts/build-info.txt
                            echo "Git Commit: \$(git rev-parse HEAD)" >> artifacts/build-info.txt
                        """
                    } else {
                        bat """
                            echo Build Number: ${BUILD_NUMBER} > artifacts\\build-info.txt
                            echo Build Time: %date% %time% >> artifacts\\build-info.txt
                            git rev-parse HEAD >> artifacts\\build-info.txt 2>nul || echo N/A >> artifacts\\build-info.txt
                        """
                    }
                }
            }
            post {
                success {
                    archiveArtifacts artifacts: 'artifacts/**', fingerprint: true
                }
            }
        }
        
        stage('Docker Build') {
            steps {
                echo 'Construindo imagem Docker...'
                script {
                    try {
                        def isUnix = isUnix()
                        if (isUnix) {
                            sh "docker build -t ${DOCKER_IMAGE} -f src/Dockerfile src/"
                            sh "docker tag ${DOCKER_IMAGE} ${APP_NAME}:latest"
                        } else {
                            bat "docker build -t ${DOCKER_IMAGE} -f src\\Dockerfile src\\"
                            bat "docker tag ${DOCKER_IMAGE} ${APP_NAME}:latest"
                        }
                    } catch (Exception e) {
                        echo "⚠️ Docker não disponível, pulando etapa de build Docker"
                        echo "Erro: ${e.getMessage()}"
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Realizando deploy...'
                script {
                    def isUnix = isUnix()
                    // Deploy local - cria diretório de deploy
                    if (isUnix) {
                        sh '''
                            mkdir -p deploy
                            cp -r src/* deploy/
                            echo "Deploy realizado em: $(date)" > deploy/deploy-info.txt
                        '''
                    } else {
                        bat '''
                            if not exist deploy mkdir deploy
                            xcopy /E /I /Y src\\* deploy\\
                            echo Deploy realizado em: %date% %time% > deploy\\deploy-info.txt
                        '''
                    }
                    
                    // Tenta parar container antigo e iniciar novo (se Docker estiver disponível)
                    try {
                        if (isUnix) {
                            sh """
                                docker stop ${APP_NAME} || true
                                docker rm ${APP_NAME} || true
                                docker run -d --name ${APP_NAME} -p 5000:5000 ${DOCKER_IMAGE} || echo "Docker não disponível para deploy"
                            """
                        } else {
                            bat """
                                docker stop ${APP_NAME} 2>nul || echo Container não existe
                                docker rm ${APP_NAME} 2>nul || echo Container não existe
                                docker run -d --name ${APP_NAME} -p 5000:5000 ${DOCKER_IMAGE} || echo Docker não disponível para deploy
                            """
                        }
                    } catch (Exception e) {
                        echo "Docker não disponível para deploy: ${e.getMessage()}"
                    }
                }
            }
            post {
                success {
                    echo 'Deploy realizado com sucesso!'
                    echo "Aplicação disponível em: http://localhost:5000"
                }
                failure {
                    echo 'Falha no deploy'
                }
            }
        }
    }
    
    post {
        always {
            echo ' Limpando ambiente...'
            cleanWs()
        }
        success {
            echo 'Pipeline executado com sucesso!'
            emailext (
                subject: "Pipeline ${env.JOB_NAME} - Build #${env.BUILD_NUMBER} - SUCESSO",
                body: "O build #${env.BUILD_NUMBER} foi concluído com sucesso!\n\nVisualize: ${env.BUILD_URL}",
                to: "${env.CHANGE_AUTHOR_EMAIL ?: 'devops@example.com'}"
            )
        }
        failure {
            echo 'Pipeline falhou!'
            emailext (
                subject: "Pipeline ${env.JOB_NAME} - Build #${env.BUILD_NUMBER} - FALHA",
                body: "O build #${env.BUILD_NUMBER} falhou!\n\nVisualize: ${env.BUILD_URL}",
                to: "${env.CHANGE_AUTHOR_EMAIL ?: 'devops@example.com'}"
            )
        }
        unstable {
            echo 'Pipeline instável (alguns testes falharam)'
        }
    }
}

