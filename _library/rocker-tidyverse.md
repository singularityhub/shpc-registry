---
layout: container
name:  "rocker/tidyverse"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/rocker/tidyverse/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/rocker/tidyverse/container.yaml"
updated_at: "2025-11-19 04:09:30.432981"
latest: "4.5.2"
container_url: "https://hub.docker.com/r/rocker/tidyverse"
aliases:
 - "R"
 - "Rscript"
 - "rocker-ml-run"
 - "rocker-tidyverse-run"
 - "rserver"
 - "rserver-pam"
 - "rsession"
 - "rstudio-server"
versions:
 - "4.2.2"
 - "3.6.3"
 - "4.1.3"
 - "4.0.5"
 - "4.2.3"
 - "4.3.0"
 - "4.3.1"
 - "4.3.2"
 - "4.3.3"
 - "4.4.0"
 - "4.4.1"
 - "4.4.2"
 - "4.4.3"
 - "4.5.0"
 - "4.5.1"
 - "4.5.2"
description: "Version-stable build of R, rstudio, and R packages "
config: {"docker": "rocker/tidyverse", "url": "https://hub.docker.com/r/rocker/tidyverse", "maintainer": "@vsoch", "description": "Version-stable build of R, rstudio, and R packages ", "latest": {"4.5.2": "sha256:dd956aa771dc72627eaeed4a87ed02843440399dcdffefb6363074b27c4c773e"}, "tags": {"4.2.2": "sha256:fa2ba674c05b42fd45b06d3f9f087d27fff934331bb67a4de91f4308d705b3ce", "3.6.3": "sha256:e3be20f79432e88e5e242d553d2bba76caf61c41d14186edd1f6a2343800de74", "4.1.3": "sha256:b5ba2c933945868adff48be3c610c0b4938d22f985a8ba355d5f03afb22e26d4", "4.0.5": "sha256:ee5aa613e706cc10d510f31f52aa68f6507d944cebbff318f0ce925e6002062b", "4.2.3": "sha256:5d76bd6ca9a0b4e364618d04ff424db9c1489d5ffef5a5df7957bd483f7a95be", "4.3.0": "sha256:747abe4759da18f321f7c62ff213e81d69abd4fc9499a402a5280d9e3bd972be", "4.3.1": "sha256:553443e1f1c12e97e2781ad93a65af63a40a85fb960175b433c6af99e138b39a", "4.3.2": "sha256:8bf33106bb56e89b71607345ac61e1db2e8eee5ce1df8679c22b13644e0e074e", "4.3.3": "sha256:b2fc0a9357b1cb6c90b7a1ac527bd09f113d76f88175db8b99d205d73fbc31b7", "4.4.0": "sha256:3e72037abda2a32d86021bbe5725e727f2c02233e4072557bc70c1e890e3471b", "4.4.1": "sha256:1af3ecf3a6072c1426ada60fb343d6d25523b0fc6390c44a3909c510b821cce8", "4.4.2": "sha256:ea10e1a66bd303807cf601b46e9a7d098dd7ceb3fe36eab0e7cef95936d7df58", "4.4.3": "sha256:da14abcd1ffa4e63093aba87a23a5cffc364e7db8f770c194965519743339760", "4.5.0": "sha256:4f41fd7b375e58fde20e00ed4d05c6eac1271314177fa22d94e1ea44d1ed1cff", "4.5.1": "sha256:c38f0fea583e3aa82d89d0038e5bb559a04fa813881031f61f6191e683954cf2", "4.5.2": "sha256:dd956aa771dc72627eaeed4a87ed02843440399dcdffefb6363074b27c4c773e"}, "filter": ["^[0-9]+[.][0-9]+[.][0-9]+$"], "aliases": {"R": "/usr/local/bin/R", "Rscript": "/usr/local/bin/Rscript", "rocker-ml-run": "/bin/bash", "rocker-tidyverse-run": "/bin/bash", "rserver": "/usr/lib/rstudio-server/bin/rserver", "rserver-pam": "/usr/lib/rstudio-server/bin/rserver-pam", "rsession": "/usr/lib/rstudio-server/bin/rsession", "rstudio-server": "/usr/lib/rstudio-server/bin/rstudio-server"}}
---

This module is a singularity container wrapper for rocker/tidyverse.
Version-stable build of R, rstudio, and R packages 
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install rocker/tidyverse
```

Or a specific version:

```bash
$ shpc install rocker/tidyverse:4.5.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load rocker/tidyverse/4.5.2
$ module help rocker/tidyverse/4.5.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tidyverse-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tidyverse-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tidyverse-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tidyverse-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tidyverse-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tidyverse-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### R

```bash
$ singularity exec <container> /usr/local/bin/R
$ podman run --it --rm --entrypoint /usr/local/bin/R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Rscript

```bash
$ singularity exec <container> /usr/local/bin/Rscript
$ podman run --it --rm --entrypoint /usr/local/bin/Rscript   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Rscript   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rocker-ml-run

```bash
$ singularity exec <container> /bin/bash
$ podman run --it --rm --entrypoint /bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rocker-tidyverse-run

```bash
$ singularity exec <container> /bin/bash
$ podman run --it --rm --entrypoint /bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rserver

```bash
$ singularity exec <container> /usr/lib/rstudio-server/bin/rserver
$ podman run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rserver-pam

```bash
$ singularity exec <container> /usr/lib/rstudio-server/bin/rserver-pam
$ podman run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rserver-pam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rserver-pam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsession

```bash
$ singularity exec <container> /usr/lib/rstudio-server/bin/rsession
$ podman run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rsession   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rsession   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rstudio-server

```bash
$ singularity exec <container> /usr/lib/rstudio-server/bin/rstudio-server
$ podman run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rstudio-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rstudio-server   -v ${PWD} -w ${PWD} <container> -c " $@"
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