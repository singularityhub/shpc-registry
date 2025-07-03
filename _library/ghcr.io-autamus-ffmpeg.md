---
layout: container
name:  "ghcr.io/autamus/ffmpeg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/ffmpeg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/ffmpeg/container.yaml"
updated_at: "2025-07-03 19:15:09.900154"
latest: "4.5"
container_url: "https://github.com/orgs/autamus/packages/container/package/ffmpeg"
aliases:
 - "ffmpeg"
 - "ffprobe"
versions:
 - "4.5"
 - "latest"
description: "FFmpeg is a free and open-source software project consisting of a large suite of libraries and programs for handling video, audio, and other multimedia files and streams."
config: {"docker": "ghcr.io/autamus/ffmpeg", "url": "https://github.com/orgs/autamus/packages/container/package/ffmpeg", "maintainer": "@vsoch", "description": "FFmpeg is a free and open-source software project consisting of a large suite of libraries and programs for handling video, audio, and other multimedia files and streams.", "latest": {"4.5": "sha256:83d07b4621380cda4c8487e029e5a57d07f408f346ed2ea46ae997783a511cc9"}, "tags": {"4.5": "sha256:83d07b4621380cda4c8487e029e5a57d07f408f346ed2ea46ae997783a511cc9", "latest": "sha256:9891b7e2e92a22b745e835d2d59dab8727a35fc2f2f86016ebb41c51e0a91cb6"}, "aliases": {"ffmpeg": "/opt/view/bin/ffmpeg", "ffprobe": "/opt/view/bin/ffprobe"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/ffmpeg.
FFmpeg is a free and open-source software project consisting of a large suite of libraries and programs for handling video, audio, and other multimedia files and streams.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/ffmpeg
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/ffmpeg:4.5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/ffmpeg/4.5
$ module help ghcr.io/autamus/ffmpeg/4.5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ffmpeg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ffmpeg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ffmpeg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ffmpeg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ffmpeg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ffmpeg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ffmpeg

```bash
$ singularity exec <container> /opt/view/bin/ffmpeg
$ podman run --it --rm --entrypoint /opt/view/bin/ffmpeg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ffmpeg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ffprobe

```bash
$ singularity exec <container> /opt/view/bin/ffprobe
$ podman run --it --rm --entrypoint /opt/view/bin/ffprobe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ffprobe   -v ${PWD} -w ${PWD} <container> -c " $@"
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