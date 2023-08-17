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
		string(defaultValue: '', name: 'L1_F132',trim: true, description: 'PART NUMBER >> L1 F132')
		string(defaultValue: '', name: 'L1_F133',trim: true, description: 'PART NUMBER >> L1 F133')
		string(defaultValue: '', name: 'L1_F194',trim: true, description: 'PART NUMBER >> L1 F194')
		string(defaultValue: '', name: 'L1_F195',trim: true, description: 'PART NUMBER >> L1 F195')
		string(defaultValue: '', name: 'L2_F132',trim: true, description: 'PART NUMBER >> L2 F132')
		string(defaultValue: '', name: 'L2_F133',trim: true, description: 'PART NUMBER >> L2 F133')
		string(defaultValue: '', name: 'L2_F194',trim: true, description: 'PART NUMBER >> L2 F194')
		string(defaultValue: '', name: 'L2_F195',trim: true, description: 'PART NUMBER >> L2 F195')
		string(defaultValue: '', name: 'L1P_F132',trim: true, description: 'PART NUMBER >> L1P F132')
		string(defaultValue: '', name: 'L1P_F133',trim: true, description: 'PART NUMBER >> L1P F133')
		string(defaultValue: '', name: 'L1P_F194',trim: true, description: 'PART NUMBER >> L1P F194')
		string(defaultValue: '', name: 'L1P_F195',trim: true, description: 'PART NUMBER >> L1P F195')		
    }
    stages {
        stage("Validate Parameters") {
            steps {
                script {
					params.each {param ->
						//if ("${param.value.trim()}" == "") {ex("'${param.key.trim()}'")}
						println " '${param.key.trim()}' -> '${param.value.trim()}' "
						env.${param.key.trim() = ${param.value.trim()}'
					}
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
