---
layout: container
name:  "quay.io/biocontainers/beagle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/beagle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/beagle/container.yaml"
updated_at: "2025-12-11 04:57:50.780693"
latest: "5.5_27Feb25.75f--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/beagle"
aliases:
 - "beagle"
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
 - "beagle_4.0_06Jun17--0"
 - "5.2_21Apr21.304--hdfd78af_0"
 - "5.1_24Aug19.3e8--hdfd78af_1"
 - "4.1_21Jan17.6cc.jar--0"
 - "4.0_06Jun17--hdfd78af_3"
 - "5.4_22Jul22.46e--hdfd78af_0"
 - "5.4_29Oct24.c8e--hdfd78af_0"
 - "5.5_27Feb25.75f--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for beagle"
config: {"url": "https://biocontainers.pro/tools/beagle", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for beagle", "latest": {"5.5_27Feb25.75f--hdfd78af_0": "sha256:503733eb23bdb0509e75298cf6524ac65437830bcceb7f7acef22e7ee6ea581d"}, "tags": {"beagle_4.0_06Jun17--0": "sha256:df38b79fcb8e3000e509ddc41c9b0aa24b28648b817de3ed6c9b0fa7bfdf1a06", "5.2_21Apr21.304--hdfd78af_0": "sha256:6c721589272492d63dc7b9c611f82545247ba8d2c26cdfa2797a7cd8493365e2", "5.1_24Aug19.3e8--hdfd78af_1": "sha256:506d72c61baacb6f906c23b7acb471aec5defa934591e600f4735bc162878484", "4.1_21Jan17.6cc.jar--0": "sha256:6efda9792b3debeab047383315567c475c64f7d3aa79f2e929a0c32e2ac61fb6", "4.0_06Jun17--hdfd78af_3": "sha256:d1d1f31ddd3044ef8733937ea63de7a249b25da9aaa465c4610bfa48d6757f74", "5.4_22Jul22.46e--hdfd78af_0": "sha256:7f84b8233f26a199ed1fa9ff898462e27d195cf08ce47d1a7780d68c984991e5", "5.4_29Oct24.c8e--hdfd78af_0": "sha256:ecd17c75c7db32466d6fd157b68ff50b2a72954c1d6007c93406f17d1be62319", "5.5_27Feb25.75f--hdfd78af_0": "sha256:503733eb23bdb0509e75298cf6524ac65437830bcceb7f7acef22e7ee6ea581d"}, "docker": "quay.io/biocontainers/beagle", "aliases": {"beagle": "/usr/local/bin/beagle", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat", "jsadebugd": "/usr/local/bin/jsadebugd", "native2ascii": "/usr/local/bin/native2ascii", "policytool": "/usr/local/bin/policytool", "appletviewer": "/usr/local/bin/appletviewer", "idlj": "/usr/local/bin/idlj", "orbd": "/usr/local/bin/orbd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/beagle.
shpc-registry automated BioContainers addition for beagle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/beagle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/beagle:5.5_27Feb25.75f--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/beagle/5.5_27Feb25.75f--hdfd78af_0
$ module help quay.io/biocontainers/beagle/5.5_27Feb25.75f--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### beagle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### beagle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### beagle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### beagle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### beagle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### beagle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### beagle

```bash
$ singularity exec <container> /usr/local/bin/beagle
$ podman run --it --rm --entrypoint /usr/local/bin/beagle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/beagle   -v ${PWD} -w ${PWD} <container> -c " $@"
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