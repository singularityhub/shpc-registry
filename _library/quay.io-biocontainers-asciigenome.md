---
layout: container
name:  "quay.io/biocontainers/asciigenome"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/asciigenome/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/asciigenome/container.yaml"
updated_at: "2023-10-04 04:49:04.248993"
latest: "1.17.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/asciigenome"
aliases:
 - "ASCIIGenome"
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
 - "1.8.0--0"
 - "1.16.0--hdfd78af_1"
 - "1.15.0--0"
 - "1.14.0--2"
 - "1.13.0--0"
 - "1.12.0--0"
 - "1.17.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for asciigenome"
config: {"url": "https://biocontainers.pro/tools/asciigenome", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for asciigenome", "latest": {"1.17.0--hdfd78af_0": "sha256:706d3699b8fe53ef2a69df01c5b9520fbd5d57cd48d5feb1facdc187f373c9e5"}, "tags": {"1.8.0--0": "sha256:0ad0505b4c6ff89bf69a28ff1d937a71afe19c1e8caa73e35553f11757f2f89c", "1.16.0--hdfd78af_1": "sha256:273eafe31a540f924b8e1a344f5366277d4b524245296a540609b48fb90b5fd0", "1.15.0--0": "sha256:6c2608b65aa6ba0978a2a46c06bcd0647e8ba9937621310f000f234cb74c9e2e", "1.14.0--2": "sha256:50b6d399ad53012a549aebe13e8830f748ba37806ed27ade651a6b8112582b7d", "1.13.0--0": "sha256:8fd1276d95e04c0a39991e128ae7793a8b3f9a5942288bd3c58b9d2691ae638c", "1.12.0--0": "sha256:632d6735989c8bc67306c61dcb5dae469faf304f0b2650a5c76a0ecfb9eb34c7", "1.17.0--hdfd78af_0": "sha256:706d3699b8fe53ef2a69df01c5b9520fbd5d57cd48d5feb1facdc187f373c9e5"}, "docker": "quay.io/biocontainers/asciigenome", "aliases": {"ASCIIGenome": "/usr/local/bin/ASCIIGenome", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat", "jsadebugd": "/usr/local/bin/jsadebugd", "native2ascii": "/usr/local/bin/native2ascii", "policytool": "/usr/local/bin/policytool", "appletviewer": "/usr/local/bin/appletviewer", "idlj": "/usr/local/bin/idlj", "orbd": "/usr/local/bin/orbd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/asciigenome.
shpc-registry automated BioContainers addition for asciigenome
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/asciigenome
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/asciigenome:1.17.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/asciigenome/1.17.0--hdfd78af_0
$ module help quay.io/biocontainers/asciigenome/1.17.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### asciigenome-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### asciigenome-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### asciigenome-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### asciigenome-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### asciigenome-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### asciigenome-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ASCIIGenome

```bash
$ singularity exec <container> /usr/local/bin/ASCIIGenome
$ podman run --it --rm --entrypoint /usr/local/bin/ASCIIGenome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ASCIIGenome   -v ${PWD} -w ${PWD} <container> -c " $@"
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