---
layout: container
name:  "quay.io/biocontainers/peptide-shaker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/peptide-shaker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/peptide-shaker/container.yaml"
updated_at: "2024-12-05 03:27:41.635393"
latest: "3.0.11--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/peptide-shaker"
aliases:
 - "peptide-shaker"
 - "easy_install-2.7"
 - "extcheck"
 - "java-rmi.cgi"
 - "javah"
 - "jhat"
 - "jsadebugd"
 - "native2ascii"
 - "policytool"
 - "appletviewer"
 - "idlj"
versions:
 - "1.16.4--py27_0"
 - "1.16.36--0"
 - "3.0.6--hdfd78af_0"
 - "2.2.25--hdfd78af_0"
 - "2.0.33--hec16e2b_1"
 - "1.16.40--1"
 - "3.0.8--hdfd78af_0"
 - "3.0.11--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for peptide-shaker"
config: {"url": "https://biocontainers.pro/tools/peptide-shaker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for peptide-shaker", "latest": {"3.0.11--hdfd78af_0": "sha256:c4ee760310934aa1eee754e68a49bf5e09592414d1b4751f24c2f9e06f6430b7"}, "tags": {"1.16.4--py27_0": "sha256:d138e3c50e8ce58ce9397a1b3d8003e5f7dd5577c7aedd56de51d1a7015fa211", "1.16.36--0": "sha256:22c90f6110139738e5955d3cec3bb98cd72a91a66f3953023431eba11cf5db90", "3.0.6--hdfd78af_0": "sha256:6be13626b6c4687c7e722f772ce03a47bbc610e6e535a98b84d5b4bc2116717d", "2.2.25--hdfd78af_0": "sha256:50b596c30d0b6e171f66787cbad65fef88ed8f437b20d86290143b207fe19a4e", "2.0.33--hec16e2b_1": "sha256:5aa9b828a3a311fb57665688d681ed9f1700f6f4fc885d7b419de461d0f168da", "1.16.40--1": "sha256:ccb8cc88f98dd7566df9ec3de6a9f6bcd60894e953f2efb53aa2dd86847187a2", "3.0.8--hdfd78af_0": "sha256:4269ab52ce6b32e311476ec7d0a340a738cb514e4909005bba282cbfcdfd3522", "3.0.11--hdfd78af_0": "sha256:c4ee760310934aa1eee754e68a49bf5e09592414d1b4751f24c2f9e06f6430b7"}, "docker": "quay.io/biocontainers/peptide-shaker", "aliases": {"peptide-shaker": "/usr/local/bin/peptide-shaker", "easy_install-2.7": "/usr/local/bin/easy_install-2.7", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat", "jsadebugd": "/usr/local/bin/jsadebugd", "native2ascii": "/usr/local/bin/native2ascii", "policytool": "/usr/local/bin/policytool", "appletviewer": "/usr/local/bin/appletviewer", "idlj": "/usr/local/bin/idlj"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/peptide-shaker.
shpc-registry automated BioContainers addition for peptide-shaker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/peptide-shaker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/peptide-shaker:3.0.11--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/peptide-shaker/3.0.11--hdfd78af_0
$ module help quay.io/biocontainers/peptide-shaker/3.0.11--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### peptide-shaker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### peptide-shaker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### peptide-shaker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### peptide-shaker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### peptide-shaker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### peptide-shaker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### peptide-shaker

```bash
$ singularity exec <container> /usr/local/bin/peptide-shaker
$ podman run --it --rm --entrypoint /usr/local/bin/peptide-shaker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peptide-shaker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-2.7

```bash
$ singularity exec <container> /usr/local/bin/easy_install-2.7
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
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