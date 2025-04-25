---
layout: container
name:  "rocker/rstudio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/rocker/rstudio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/rocker/rstudio/container.yaml"
updated_at: "2025-04-25 03:00:00.901740"
latest: "4.5.0"
container_url: "https://hub.docker.com/r/rocker/rstudio"
aliases:
 - "R"
 - "Rscript"
 - "rocker-rstudio-run"
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
description: "Rstudio server image"
config: {"docker": "rocker/rstudio", "url": "https://hub.docker.com/r/rocker/rstudio", "maintainer": "@vsoch", "description": "Rstudio server image", "latest": {"4.5.0": "sha256:2aacb0da78890fb7615744765ca1bd3b57e991c347c7ce26adb1b9243a20b781"}, "tags": {"4.2.2": "sha256:2b50f9f8c567a6b861c2e2979ab5ff6803df9d27385e9da9c117d3a8a65576a4", "3.6.3": "sha256:a2014be0cc26059c3f7fbbef66b25599b7c8871f880caac12037f9a142f60b81", "4.1.3": "sha256:a44a63194c7c30cb19f731ab226a926c3a5bef086a4331e3f4cb770ac51c6ec4", "4.0.5": "sha256:0f3da9a4708fa208c3abe215aa77e3b96b7ebbf3b5e646c97539df53abc97a92", "4.2.3": "sha256:bddad1808b2efd8bad447ae119ef0fe2f6e02f619b003add0e49b9edb4b75477", "4.3.0": "sha256:9b45914ee71c1f938d52011b00d6ed883a2ad9265543fb65372cf2647daebf98", "4.3.1": "sha256:f0d21d64efa92ddc0d5f5ffa8be4173353d70140407e0c7bdc2c750fab007fdd", "4.3.2": "sha256:2f48314dfffab8ac2e1bc1797b0564b1f96927f702c064ab2cc69ce1b1c62016", "4.3.3": "sha256:9c11789a414fa884bec44e8c218909516d9b5a3f232d3f5d59155521d0975d18", "4.4.0": "sha256:8b41166f8c02e1c367d4862dcb3f68dd6f02cd47b41ad66f86bcc288960d5e28", "4.4.1": "sha256:051c070473e7e29508673daf64d10d78f44506fd0c84e83e9471a1900c885c4b", "4.4.2": "sha256:6bfc87fb66d0072e28d88d684a1f7b3e42a1c20360ee5eca5b43168a4eba3945", "4.4.3": "sha256:8e0b919afc4032904412f914b63164bc29ed744edb27618530df3ca83f098c65", "4.5.0": "sha256:2aacb0da78890fb7615744765ca1bd3b57e991c347c7ce26adb1b9243a20b781"}, "filter": ["^[0-9]+[.][0-9]+[.][0-9]+$"], "aliases": {"R": "/usr/local/bin/R", "Rscript": "/usr/local/bin/Rscript", "rocker-rstudio-run": "/bin/bash", "rserver": "/usr/lib/rstudio-server/bin/rserver", "rserver-pam": "/usr/lib/rstudio-server/bin/rserver-pam", "rsession": "/usr/lib/rstudio-server/bin/rsession", "rstudio-server": "/usr/lib/rstudio-server/bin/rstudio-server"}}
---

This module is a singularity container wrapper for rocker/rstudio.
Rstudio server image
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install rocker/rstudio
```

Or a specific version:

```bash
$ shpc install rocker/rstudio:4.5.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load rocker/rstudio/4.5.0
$ module help rocker/rstudio/4.5.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rstudio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rstudio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rstudio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rstudio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rstudio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rstudio-inspect-deffile:

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


#### rocker-rstudio-run

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