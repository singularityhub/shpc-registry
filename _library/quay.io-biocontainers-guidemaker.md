---
layout: container
name:  "quay.io/biocontainers/guidemaker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/guidemaker/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/guidemaker/container.yaml"
updated_at: "2022-10-27 00:27:20.022746"
latest: "0.3.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/guidemaker"
aliases:
 - "base58"
 - "black-primer"
 - "elasticurl"
 - "elasticurl_cpp"
 - "elastipubsub"
 - "guidemaker"
 - "onnxruntime_test"
 - "pdoc"
 - "pdoc3"
 - "streamlit"
 - "streamlit.cmd"
 - "watchmedo"
versions:
 - "0.3.4--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for guidemaker"
config: {"url": "https://biocontainers.pro/tools/guidemaker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for guidemaker", "latest": {"0.3.4--pyhdfd78af_0": "sha256:9ffc309a7fdc7dad98bca348e8d6ca538548b2e0ca4b24961c88f40fdcb6c83d"}, "tags": {"0.3.4--pyhdfd78af_0": "sha256:9ffc309a7fdc7dad98bca348e8d6ca538548b2e0ca4b24961c88f40fdcb6c83d"}, "docker": "quay.io/biocontainers/guidemaker", "aliases": {"base58": "/usr/local/bin/base58", "black-primer": "/usr/local/bin/black-primer", "elasticurl": "/usr/local/bin/elasticurl", "elasticurl_cpp": "/usr/local/bin/elasticurl_cpp", "elastipubsub": "/usr/local/bin/elastipubsub", "guidemaker": "/usr/local/bin/guidemaker", "onnxruntime_test": "/usr/local/bin/onnxruntime_test", "pdoc": "/usr/local/bin/pdoc", "pdoc3": "/usr/local/bin/pdoc3", "streamlit": "/usr/local/bin/streamlit", "streamlit.cmd": "/usr/local/bin/streamlit.cmd", "watchmedo": "/usr/local/bin/watchmedo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/guidemaker.
shpc-registry automated BioContainers addition for guidemaker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/guidemaker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/guidemaker:0.3.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/guidemaker/0.3.4--pyhdfd78af_0
$ module help quay.io/biocontainers/guidemaker/0.3.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### guidemaker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### guidemaker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### guidemaker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### guidemaker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### guidemaker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### guidemaker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### base58

```bash
$ singularity exec <container> /usr/local/bin/base58
$ podman run --it --rm --entrypoint /usr/local/bin/base58   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base58   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### black-primer

```bash
$ singularity exec <container> /usr/local/bin/black-primer
$ podman run --it --rm --entrypoint /usr/local/bin/black-primer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/black-primer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl

```bash
$ singularity exec <container> /usr/local/bin/elasticurl
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl_cpp

```bash
$ singularity exec <container> /usr/local/bin/elasticurl_cpp
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastipubsub

```bash
$ singularity exec <container> /usr/local/bin/elastipubsub
$ podman run --it --rm --entrypoint /usr/local/bin/elastipubsub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastipubsub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guidemaker

```bash
$ singularity exec <container> /usr/local/bin/guidemaker
$ podman run --it --rm --entrypoint /usr/local/bin/guidemaker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guidemaker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### onnxruntime_test

```bash
$ singularity exec <container> /usr/local/bin/onnxruntime_test
$ podman run --it --rm --entrypoint /usr/local/bin/onnxruntime_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/onnxruntime_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdoc

```bash
$ singularity exec <container> /usr/local/bin/pdoc
$ podman run --it --rm --entrypoint /usr/local/bin/pdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdoc3

```bash
$ singularity exec <container> /usr/local/bin/pdoc3
$ podman run --it --rm --entrypoint /usr/local/bin/pdoc3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdoc3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamlit

```bash
$ singularity exec <container> /usr/local/bin/streamlit
$ podman run --it --rm --entrypoint /usr/local/bin/streamlit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamlit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamlit.cmd

```bash
$ singularity exec <container> /usr/local/bin/streamlit.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/streamlit.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamlit.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchmedo

```bash
$ singularity exec <container> /usr/local/bin/watchmedo
$ podman run --it --rm --entrypoint /usr/local/bin/watchmedo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchmedo   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)