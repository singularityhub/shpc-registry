---
layout: container
name:  "quay.io/biocontainers/peptide-shaker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/peptide-shaker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/peptide-shaker/container.yaml"
updated_at: "2023-09-22 03:06:19.955961"
latest: "1.16.36--0"
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
description: "shpc-registry automated BioContainers addition for peptide-shaker"
config: {"url": "https://biocontainers.pro/tools/peptide-shaker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for peptide-shaker", "latest": {"1.16.36--0": "sha256:517b09a0af52899fd1143053d06595b8e2dbddbe1c4b3cf717018e2ea6edc4ab"}, "tags": {"1.16.4--py27_0": "sha256:1ee91304befdc6a6b3573eadfd25ff59ec64f4f08c909b0e95a3edfa4e3d0617", "1.16.36--0": "sha256:517b09a0af52899fd1143053d06595b8e2dbddbe1c4b3cf717018e2ea6edc4ab"}, "docker": "quay.io/biocontainers/peptide-shaker", "aliases": {"peptide-shaker": "/usr/local/bin/peptide-shaker", "easy_install-2.7": "/usr/local/bin/easy_install-2.7", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat", "jsadebugd": "/usr/local/bin/jsadebugd", "native2ascii": "/usr/local/bin/native2ascii", "policytool": "/usr/local/bin/policytool", "appletviewer": "/usr/local/bin/appletviewer", "idlj": "/usr/local/bin/idlj"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/peptide-shaker.
shpc-registry automated BioContainers addition for peptide-shaker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/peptide-shaker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/peptide-shaker:1.16.36--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/peptide-shaker/1.16.36--0
$ module help quay.io/biocontainers/peptide-shaker/1.16.36--0
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