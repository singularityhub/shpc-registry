---
layout: container
name:  "quay.io/biocontainers/trinity"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/trinity/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/trinity/container.yaml"
updated_at: "2023-10-23 03:14:22.875093"
latest: "date.2011_11_26--ncurses5.9_8"
container_url: "https://biocontainers.pro/tools/trinity"
aliases:
 - "trinity"
 - "Trinity"
 - "Trinity-test"
 - "perl5.22.0"
 - "c2ph"
 - "pstruct"
 - "extcheck"
 - "java-rmi.cgi"
 - "javah"
 - "jhat"
 - "jsadebugd"
 - "native2ascii"
 - "policytool"
versions:
 - "2.11.0--h5ef6573_1"
 - "2.12.0--ha140323_3"
 - "2.13.2--hea94271_3"
 - "date.2011_11_26--ncurses5.9_8"
 - "2.15.1--hff880f7_1"
 - "2.13.2--hff880f7_4"
 - "2.15.1--h6ab5fc9_2"
 - "2.15.1--pl5321h146fbdb_3"
description: "shpc-registry automated BioContainers addition for trinity"
config: {"url": "https://biocontainers.pro/tools/trinity", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for trinity", "latest": {"date.2011_11_26--ncurses5.9_8": "sha256:eabe346a2adac1bb30aaaa62764f299638daa2a83ef6408722b0f89f8c490e20"}, "tags": {"2.11.0--h5ef6573_1": "sha256:6d35d716aa12ba7b0c715fa8a30359b43ba9151e854dc4407b949e7b57c3a50a", "2.12.0--ha140323_3": "sha256:d44cb9353096e558adf34f4b6219c252d6b3523db9555c7dbecd0ed980e68d58", "2.13.2--hea94271_3": "sha256:9107340bc575f8ec80dee7814f325217c3fa51d15f2fc30e9907606fa289f88a", "date.2011_11_26--ncurses5.9_8": "sha256:eabe346a2adac1bb30aaaa62764f299638daa2a83ef6408722b0f89f8c490e20", "2.15.1--hff880f7_1": "sha256:cbf4fc1f67b4d1d20ad00f89c9a18774b152d1b46a45b666c64cfb594e1f6346", "2.13.2--hff880f7_4": "sha256:e6352a3026242bdb0102038d98854b220b13ffab3b254de539b05c2b56eb007e", "2.15.1--h6ab5fc9_2": "sha256:494af74f4a1ea05396780f78a5ef3cc22be401ea7906a7ea42d68bf9c6af770a", "2.15.1--pl5321h146fbdb_3": "sha256:b936ffb3935c5a973730995c648389db823f0ce40c17c4ac52dfbafec00d8cb6"}, "docker": "quay.io/biocontainers/trinity", "aliases": {"trinity": "/usr/local/bin/Trinity", "Trinity": "/usr/local/bin/Trinity", "Trinity-test": "/usr/local/bin/Trinity-test", "perl5.22.0": "/usr/local/bin/perl5.22.0", "c2ph": "/usr/local/bin/c2ph", "pstruct": "/usr/local/bin/pstruct", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat", "jsadebugd": "/usr/local/bin/jsadebugd", "native2ascii": "/usr/local/bin/native2ascii", "policytool": "/usr/local/bin/policytool"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/trinity.
shpc-registry automated BioContainers addition for trinity
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/trinity
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/trinity:date.2011_11_26--ncurses5.9_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/trinity/date.2011_11_26--ncurses5.9_8
$ module help quay.io/biocontainers/trinity/date.2011_11_26--ncurses5.9_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### trinity-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### trinity-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### trinity-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### trinity-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### trinity-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### trinity-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### trinity

```bash
$ singularity exec <container> /usr/local/bin/Trinity
$ podman run --it --rm --entrypoint /usr/local/bin/Trinity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Trinity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Trinity

```bash
$ singularity exec <container> /usr/local/bin/Trinity
$ podman run --it --rm --entrypoint /usr/local/bin/Trinity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Trinity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Trinity-test

```bash
$ singularity exec <container> /usr/local/bin/Trinity-test
$ podman run --it --rm --entrypoint /usr/local/bin/Trinity-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Trinity-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.22.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.22.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c2ph

```bash
$ singularity exec <container> /usr/local/bin/c2ph
$ podman run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pstruct

```bash
$ singularity exec <container> /usr/local/bin/pstruct
$ podman run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
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