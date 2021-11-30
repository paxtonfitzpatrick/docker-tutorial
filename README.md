[Slides](https://github.com/paxtonfitzpatrick/docker-tutorial/tree/main/slides) 
and example files for the [FINN Lab](https://thefinnlab.github.io/) Docker 
tutorial. The pre-built analyses image is available on [Docker Hub](https://hub.docker.com/), 
[here](https://hub.docker.com/repository/docker/paxtonfitzpatrick/tutorial-image).

**Note**: the files in this repo are designed to be simplified examples. If 
you're looking for ready-to-use images or template Dockerfiles, check out the 
[CDL-docker-stacks](https://github.com/ContextLab/CDL-docker-stacks) repo
(pre-built images are on Docker Hub [here](https://hub.docker.com/u/contextlab))

### Installing Docker:
You can install Docker using one of the guides below:
- [MacOS](https://docs.docker.com/desktop/mac/install/) (Intel or Apple chip)
- [Windows](https://docs.docker.com/desktop/windows/install/)
- [Linux](https://docs.docker.com/engine/install/)

You do not need to create a Docker ID or any accounts for this tutorial.

### Cloning this repository:
```shell
git clone --recursive https://github.com/paxtonfitzpatrick/docker-tutorial.git
```
The `--recursive` flag is needed because the `experiment` directory is a 
submodule linked to 
[paxtonfitzpatrick/psiturk-experiment-template](https://github.com/paxtonfitzpatrick/psiturk-experiment-template).
If you cloned this repo without the `--recursive` flag and your `experiment` 
folder is empty, you can fix this by `cd`ing into your local repo and pulling 
the submodule with
```shell
git submodule update --init --recursive
```
