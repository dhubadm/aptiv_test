def ex(param){
    currentBuild.result = 'ABORTED'
    error('NULL PARAM: ' + param)
}

pipeline {
    agent any
    parameters {
        choice(choices: ['DT', 'WS', 'WL74', 'WL75'], name: 'BUILD', description: 'Build type: WS|DT|WL75|WL74')
        string(defaultValue: '0x01', name: 'PATCH',trim: true, description: 'Provide PATCH as 0x..')	
	string(defaultValue: '', name: 'VERSION',trim: true, description: 'Provide VERSION number...')
    }
    stages {
        stage("Validate Parameters") {
            steps {
                script {
					params.each {param ->
						//if ("${param.value.trim()}" == "") {ex("'${param.key.trim()}'")}
						println " '${param.key.trim()}' -> '${param.value.trim()}' "
						eval "env.${param.key.trim()}=${param.value.trim()}"
					}
			println "${kv}"
                }
            }
        }
        stage('Pre-Build') {
            steps {
                echo 'Hello World'
                sh 'python3 --version'
            }
        }
		stage('Build') {
			steps {
				script{
					env.TEST = 'a,b,c'
					ACTIVE_CONNECTORS = sh(script: """
										python3 -c "import os;\
										print(os.environ['TEST'])"
										""".stripIndent(), returnStdout: true).trim()
					println ACTIVE_CONNECTORS
					sh 'ls -lart; printenv'
					sh 'pwd;python3 test.py;ls -lart'
				}
			}
			post {
				always {
					echo "${params.BUILD}"
				}
				failure {
					//mail to: team@example.com, subject: 'The Pipeline failed :('
					echo "ERROR...."
				}
			}
		}
    }
}
