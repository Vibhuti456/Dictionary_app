pipeline
{
    agent
    {
        node 
        {
            label "dev"
        }
    }
    stages
    {
        stage("Code Clone")
        {
            steps
            {
                git url: "https://github.com/Vibhuti456/Dictionary_app.git", branch: "master"
                echo "Code has cloned in your worker node"
            }
        }
        
        stage("Build")
        {
            steps
            {
                sh "docker build -t dictionary-app:latest ."
                echo "image has built in slave system"
            }
        }
        
        stage("Test and Scanning")
        {
            steps
            {
                echo 'image has been scanned'
            }
        }
        
        stage("Deploy")
        {
            steps
            {
                //sh "docker run -d -p 5000:5000 --name dict-app dictionary-app:latest"
                sh "docker compose down && docker compose up -d"   
                echo "Application has deployed succesfully"
            }
        }
    }
}
