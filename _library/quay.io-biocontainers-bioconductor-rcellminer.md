---
layout: container
name:  "quay.io/biocontainers/bioconductor-rcellminer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rcellminer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rcellminer/container.yaml"
updated_at: "2023-10-03 03:12:45.708047"
latest: "2.22.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rcellminer"
aliases:
 - "extcheck"
 - "java-rmi.cgi"
 - "javah"
 - "jhat"
 - "jsadebugd"
 - "native2ascii"
 - "policytool"
 - "appletviewer"
 - "idlj"
 - "orbd"
versions:
 - "2.8.0--r36_1"
 - "2.20.0--r42hdfd78af_0"
 - "2.16.0--r41hdfd78af_0"
 - "2.14.0--r41hdfd78af_0"
 - "2.12.1--r40hdfd78af_0"
 - "2.11.1--r40_0"
 - "2.22.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rcellminer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rcellminer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rcellminer", "latest": {"2.22.0--r43hdfd78af_0": "sha256:40d0e8b037bee66ec887f318c8cd57d6471670df836fb6e4c66794a6895b577c"}, "tags": {"2.8.0--r36_1": "sha256:b927a7912ea2f428e2e8824ff0146656b4bbb6517a11fd94a30286e319a2beee", "2.20.0--r42hdfd78af_0": "sha256:bc265f7c224bde31f4571ef5c9c542d965a80c1a66d5c12d6951b6db7172bb51", "2.16.0--r41hdfd78af_0": "sha256:d3e18b923db23a9b6afe2203520b4ec476ca79997eed92de2360ae9bf9a7d1c1", "2.14.0--r41hdfd78af_0": "sha256:f42c29c2bfb015b883d7319b84fd69a8152481c2c2df761643f31e19d3848a9d", "2.12.1--r40hdfd78af_0": "sha256:972127e1428c9dddd8daf76847131a880a2c90ad50a674becf329407e1433e2e", "2.11.1--r40_0": "sha256:8bac4aadf600be3eff84f86bec00a3e93848029d9b7e126818088d9857397587", "2.22.0--r43hdfd78af_0": "sha256:40d0e8b037bee66ec887f318c8cd57d6471670df836fb6e4c66794a6895b577c"}, "docker": "quay.io/biocontainers/bioconductor-rcellminer", "aliases": {"extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat", "jsadebugd": "/usr/local/bin/jsadebugd", "native2ascii": "/usr/local/bin/native2ascii", "policytool": "/usr/local/bin/policytool", "appletviewer": "/usr/local/bin/appletviewer", "idlj": "/usr/local/bin/idlj", "orbd": "/usr/local/bin/orbd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rcellminer.
shpc-registry automated BioContainers addition for bioconductor-rcellminer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rcellminer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rcellminer:2.22.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rcellminer/2.22.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rcellminer/2.22.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rcellminer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rcellminer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rcellminer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rcellminer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rcellminer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rcellminer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### extcheck

```bash
$ singularity exec <container> /usr/local/bin/extcheck
$ podman run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### java-rmi.cgi

```bash
$ singularity exec <container> /usr/local/bin/java-rmi.cgi
$ podman run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javah

```bash
$ singularity exec <container> /usr/local/bin/javah
$ podman run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhat

```bash
$ singularity exec <container> /usr/local/bin/jhat
$ podman run --it --rm --entrypoint /usr/local/bin/jhat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsadebugd

```bash
$ singularity exec <container> /usr/local/bin/jsadebugd
$ podman run --it --rm --entrypoint /usr/local/bin/jsadebugd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsadebugd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### native2ascii

```bash
$ singularity exec <container> /usr/local/bin/native2ascii
$ podman run --it --rm --entrypoint /usr/local/bin/native2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/native2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### policytool

```bash
$ singularity exec <container> /usr/local/bin/policytool
$ podman run --it --rm --entrypoint /usr/local/bin/policytool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/policytool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### appletviewer

```bash
$ singularity exec <container> /usr/local/bin/appletviewer
$ podman run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idlj

```bash
$ singularity exec <container> /usr/local/bin/idlj
$ podman run --it --rm --entrypoint /usr/local/bin/idlj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idlj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orbd

```bash
$ singularity exec <container> /usr/local/bin/orbd
$ podman run --it --rm --entrypoint /usr/local/bin/orbd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orbd   -v ${PWD} -w ${PWD} <container> -c " $@"
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