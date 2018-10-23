germaniumPyExePipeline([
    runFlake8: false,

    binaries: [
        "linux64": [
            dockerTag: "thrifty",
            exe: "/src/dist/thrifty",
            publishPypi: true
        ]
    ],

    postBuild: {
        stage('Report Tests') {
            node {
                docker.image('thrifty').inside {
                    sh "cp /src/nose2-junit.xml ${pwd()}"
                    junit 'nose2-junit.xml'
                }
            }
        }
    }
])
