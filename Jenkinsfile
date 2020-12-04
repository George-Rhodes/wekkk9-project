pipeline{
    agent any

	stages{
		stage('Install Docker using ansible'){
            steps{
                sh ". ./scripts/ansible.sh"
                	}
            	}
		stage ('Test application'){
			steps{
				sh ". ./scripts/tests.sh"
			} 
		}
		stage ('Push Docker'){
            steps{
                sh ". ./scripts/build.sh"
                        }
                }
        stage('Deploy application'){
            steps{
                sh ". ./scripts/deploy.sh"

                        }

        	}
	}
}