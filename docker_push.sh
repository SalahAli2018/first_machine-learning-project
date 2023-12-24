# Get the latest tag from the GitHub repository
latest_tag=$(git describe --tags --abbrev=0)
echo $latest_tag
# Build and push the Docker image with the same tag
docker build -t salahali2018/first-machine-learning-container:$latest_tag .
# # docker login -u salahali2018 -p ${Docker_Hub_Password}
docker push salahali2018/first-machine-learning-container:$latest_tag
