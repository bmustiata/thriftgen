germaniumPyExePipeline([
    runFlake8: false,
    publishPublicPyPi: true,

    binaries: [
        "linux64": [
            dockerTag: "thrifty",
            exe: "/src/dist/thrifty"
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
