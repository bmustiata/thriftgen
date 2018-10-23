germaniumPyExePipeline([
    runFlake8: false,

    binaries: [
        "linux64": [
            dockerTag: "thriftgen",
            exe: "/src/dist/thriftgen",
            publishPypi: "sdist"
        ]
    ],

    postBuild: {
        stage('Report Tests') {
            node {
                docker.image('thriftgen').inside {
                    sh "cp /src/nose2-junit.xml ${pwd()}"
                    junit 'nose2-junit.xml'
                }
            }
        }
    }
])
