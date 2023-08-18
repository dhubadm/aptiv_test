def ex(param){
    currentBuild.result = 'ABORTED'
    error('NULL PARAM: ' + param)
}

pipeline {
    agent any
    parameters {
        choice(choices: ['DT', 'WS', 'WL74', 'WL75'], name: 'BUILD', description: 'Build type: WS|DT|WL75|WL74')
        string(defaultValue: '0x01', name: 'PATCH',trim: true, description: 'Provide PATCH as 0x..')	
		string(defaultValue: 'DUMMY', name: 'RELEASE_VERSION',trim: true, description: 'Provide VERSION number...')
		//BUILD PART numbers parameters
		string(defaultValue: '0383648AEF909093494', name: 'L1_F132',trim: true, description: 'PART NUMBER >> L1 F132')
		string(defaultValue: '99999AFS99', name: 'L1_F133',trim: true, description: 'PART NUMBER >> L1 F133')
		string(defaultValue: '202020YZ', name: 'L1_F194',trim: true, description: 'PART NUMBER >> L1 F194')
		string(defaultValue: '20', name: 'L1_F195',trim: true, description: 'PART NUMBER >> L1 F195')
		string(defaultValue: '9093494', name: 'L2_F132',trim: true, description: 'PART NUMBER >> L2 F132')
		string(defaultValue: '8363721', name: 'L2_F133',trim: true, description: 'PART NUMBER >> L2 F133')
		string(defaultValue: '202020YZ', name: 'L2_F194',trim: true, description: 'PART NUMBER >> L2 F194')
		string(defaultValue: '38', name: 'L2_F195',trim: true, description: 'PART NUMBER >> L2 F195')
		string(defaultValue: '0383609093494', name: 'L1P_F132',trim: true, description: 'PART NUMBER >> L1P F132')
		string(defaultValue: 'e7878272e', name: 'L1P_F133',trim: true, description: 'PART NUMBER >> L1P F133')
		string(defaultValue: '20dd2020YZ', name: 'L1P_F194',trim: true, description: 'PART NUMBER >> L1P F194')
		string(defaultValue: '08', name: 'L1P_F195',trim: true, description: 'PART NUMBER >> L1P F195')
		//BST BUILD tool parameters
		string(defaultValue: '10.15.46.0', name: 'TRACKER_360',trim: true, description: 'BST Tool version')
		string(defaultValue: '6.6.3.28', name: 'SATA',trim: true, description: 'BST Build Tool version')
		string(defaultValue: '16.27.0.8', name: 'SPP_OTP',trim: true, description: 'BST Build Tool version')
		string(defaultValue: '18.0.0.0', name: 'VSE',trim: true, description: 'BST Build Tool version')
		//JIRA FD22 Module parameters
		string(defaultValue: '3.1.0', name: 'ADAPTIVE_CRUISE_CONTROL',trim: true, description: 'Values taken from JIRA Ticket')
		string(defaultValue: '36.0.2', name: 'COLLISION_AVOIDANCE',trim: true, description: 'Values taken from JIRA Ticket')
		string(defaultValue: '2.1.0', name: 'INHIBIT_MANAGER',trim: true, description: 'Values taken from JIRA Ticket')
		string(defaultValue: '1.2.1', name: 'HMI',trim: true, description: 'Values taken from JIRA Ticket')
		string(defaultValue: '2754', name: 'LATERAL_CONTROL',trim: true, description: 'Values taken from JIRA Ticket')
		string(defaultValue: '2772', name: 'SIDE_FEATURES',trim: true, description: 'Values taken from JIRA Ticket')
		string(defaultValue: '1117', name: 'INPUT_WRAPPER',trim: true, description: 'Values taken from JIRA Ticket')
		string(defaultValue: '325', name: 'OUTPUT_WRAPPER',trim: true, description: 'Values taken from JIRA Ticket')
		string(defaultValue: '1213', name: 'VEHICLE_STATUS',trim: true, description: 'Values taken from JIRA Ticket')
		string(defaultValue: '1921', name: 'SAF',trim: true, description: 'Values taken from JIRA Ticket')
	}
    stages {
        stage("Validate Parameters") {
            steps {
                script {
					params.each {param ->
						//if ("${param.value.trim()}" == "") {ex("'${param.key.trim()}'")}
						print " '${param.key.trim()}' -> '${param.value.trim()}' "
						//sh 'eval "env.${param.key.trim()}=${param.value.trim()}"'
					}
                }
            }
        }
        stage('Pre-Build') {
            steps {
		load "envVars.groovy"
                echo 'Hello World'
                sh 'python3 --version; printenv'
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
					//sh 'ls -lart; printenv'
					//sh 'pwd;python3 test.py;ls -lart'
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
