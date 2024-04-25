---
layout: container
name:  "quay.io/biocontainers/ena-webin-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ena-webin-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ena-webin-cli/container.yaml"
updated_at: "2024-04-25 02:59:31.479759"
latest: "6.7.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/ena-webin-cli"
aliases:
 - "ena-webin-cli"
 - "clhsdb"
 - "hsdb"
 - "extcheck"
 - "java-rmi.cgi"
 - "javah"
 - "jhat"
 - "jsadebugd"
 - "native2ascii"
 - "policytool"
 - "appletviewer"
versions:
 - "5.0.0--hdfd78af_0"
 - "6.5.1--hdfd78af_0"
 - "6.7.1--hdfd78af_0"
 - "6.6.0--hdfd78af_0"
 - "6.7.2--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for ena-webin-cli"
config: {"url": "https://biocontainers.pro/tools/ena-webin-cli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ena-webin-cli", "latest": {"6.7.2--hdfd78af_0": "sha256:61bcffcc6df9797bfb17dcbd760563096a7d766019a34e919ddf07bba794b445"}, "tags": {"5.0.0--hdfd78af_0": "sha256:ad7da743b67738b93d0d87d11c2edd9c8183d31687057bfb10a6d33fae9eff96", "6.5.1--hdfd78af_0": "sha256:7cc84dd62b5ba940c388dce000cb24bc87b9de88db51035275dab7091248cb36", "6.7.1--hdfd78af_0": "sha256:c430af9b6784e43fb1a1ec5e907c4753f1c02498539eba35f31c08c63a7aa631", "6.6.0--hdfd78af_0": "sha256:e932b5ad82b35521f0ed7dad80561801965585e428aed4dbd3b9caa4b2f65c9d", "6.7.2--hdfd78af_0": "sha256:61bcffcc6df9797bfb17dcbd760563096a7d766019a34e919ddf07bba794b445"}, "docker": "quay.io/biocontainers/ena-webin-cli", "aliases": {"ena-webin-cli": "/usr/local/bin/ena-webin-cli", "clhsdb": "/usr/local/bin/clhsdb", "hsdb": "/usr/local/bin/hsdb", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat", "jsadebugd": "/usr/local/bin/jsadebugd", "native2ascii": "/usr/local/bin/native2ascii", "policytool": "/usr/local/bin/policytool", "appletviewer": "/usr/local/bin/appletviewer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ena-webin-cli.
shpc-registry automated BioContainers addition for ena-webin-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ena-webin-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ena-webin-cli:6.7.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ena-webin-cli/6.7.2--hdfd78af_0
$ module help quay.io/biocontainers/ena-webin-cli/6.7.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ena-webin-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ena-webin-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ena-webin-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ena-webin-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ena-webin-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ena-webin-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ena-webin-cli

```bash
$ singularity exec <container> /usr/local/bin/ena-webin-cli
$ podman run --it --rm --entrypoint /usr/local/bin/ena-webin-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ena-webin-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clhsdb

```bash
$ singularity exec <container> /usr/local/bin/clhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/clhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hsdb

```bash
$ singularity exec <container> /usr/local/bin/hsdb
$ podman run --it --rm --entrypoint /usr/local/bin/hsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
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