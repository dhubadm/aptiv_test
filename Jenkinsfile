def ex(param){
    currentBuild.result = 'ABORTED'
    error('NULL PARAM: ' + param)
}

pipeline {
    agent any
    parameters {
        choice(choices: ['DT', 'WS', 'WL74', 'WL75'], name: 'BUILD', description: 'Build type: WS|DT|WL75|WL74')
        string(defaultValue: '0x01', name: 'PATCH',trim: true, description: 'Provide PATCH as 0x..')	
		string(defaultValue: '', name: 'RELEASE_VERSION',trim: true, description: 'Provide VERSION number...')
		//BUILD PART numbers parameters
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
		//BST BUILD tool parameters
		string(defaultValue: '10.15.46.0', name: 'TRACKER_360',trim: true, description: 'BST Tool version')
		string(defaultValue: '6.6.3.28', name: 'SATA',trim: true, description: 'BST Build Tool version')
		string(defaultValue: '16.27.0.8', name: 'SPP_OTP',trim: true, description: 'BST Build Tool version')
		string(defaultValue: '18.0.0.0', name: 'VSE',trim: true, description: 'BST Build Tool version')
		//JIRA FD22 Module parameters
		string(defaultValue: '', name: 'ADAPTIVE_CRUISE_CONTROL',trim: true, description: 'Values taken from JIRA Ticket')
		string(defaultValue: '', name: 'COLLISION_AVOIDANCE',trim: true, description: 'Values taken from JIRA Ticket')
		string(defaultValue: '', name: 'INHIBIT_MANAGER',trim: true, description: 'Values taken from JIRA Ticket')
		string(defaultValue: '', name: 'HMI',trim: true, description: 'Values taken from JIRA Ticket')
		string(defaultValue: '', name: 'LATERAL_CONTROL',trim: true, description: 'Values taken from JIRA Ticket')
		string(defaultValue: '', name: 'SIDE_FEATURES',trim: true, description: 'Values taken from JIRA Ticket')
		string(defaultValue: '', name: 'INPUT_WRAPPER',trim: true, description: 'Values taken from JIRA Ticket')
		string(defaultValue: '', name: 'OUTPUT_WRAPPER',trim: true, description: 'Values taken from JIRA Ticket')
		string(defaultValue: '', name: 'VEHICLE_STATUS',trim: true, description: 'Values taken from JIRA Ticket')
		string(defaultValue: '', name: 'SAF',trim: true, description: 'Values taken from JIRA Ticket')
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
                //Stage will handle File_Data.h
                sh 'python3 --version'
		sh 'pwd;python3 test.py;ls -lart'
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
					//Stage will run BUILD
					//sh 'python3 aptiv_host_build.py -cache -variant dt -include_spp_otp -cores 16 build -lib ALL -capp -app -no_ds -hll'
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
