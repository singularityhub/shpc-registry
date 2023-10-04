---
layout: container
name:  "quay.io/biocontainers/chromhmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chromhmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chromhmm/container.yaml"
updated_at: "2023-10-04 05:07:38.603547"
latest: "1.24--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/chromhmm"
aliases:
 - "ChromHMM.sh"
 - "download_chromhmm_data.sh"
 - "funzip"
 - "unzipsfx"
 - "zipgrep"
 - "zipinfo"
 - "unzip"
 - "jfr"
 - "jaotc"
 - "aserver"
 - "jdeprscan"
 - "jhsdb"
versions:
 - "1.23--hdfd78af_0"
 - "1.24--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for chromhmm"
config: {"url": "https://biocontainers.pro/tools/chromhmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for chromhmm", "latest": {"1.24--hdfd78af_0": "sha256:faa842647a2fd38569b6901ceaaea9e2b24ff69907debce0a0f16f49e5a1ec8f"}, "tags": {"1.23--hdfd78af_0": "sha256:e946f36b053df17ad5650dd13b6616e090d7eca40e088e8f7ffa2a87a8ddf2b3", "1.24--hdfd78af_0": "sha256:faa842647a2fd38569b6901ceaaea9e2b24ff69907debce0a0f16f49e5a1ec8f"}, "docker": "quay.io/biocontainers/chromhmm", "aliases": {"ChromHMM.sh": "/usr/local/bin/ChromHMM.sh", "download_chromhmm_data.sh": "/usr/local/bin/download_chromhmm_data.sh", "funzip": "/usr/local/bin/funzip", "unzipsfx": "/usr/local/bin/unzipsfx", "zipgrep": "/usr/local/bin/zipgrep", "zipinfo": "/usr/local/bin/zipinfo", "unzip": "/usr/local/bin/unzip", "jfr": "/usr/local/bin/jfr", "jaotc": "/usr/local/bin/jaotc", "aserver": "/usr/local/bin/aserver", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chromhmm.
shpc-registry automated BioContainers addition for chromhmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chromhmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chromhmm:1.24--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chromhmm/1.24--hdfd78af_0
$ module help quay.io/biocontainers/chromhmm/1.24--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chromhmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chromhmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chromhmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chromhmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chromhmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chromhmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ChromHMM.sh

```bash
$ singularity exec <container> /usr/local/bin/ChromHMM.sh
$ podman run --it --rm --entrypoint /usr/local/bin/ChromHMM.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ChromHMM.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download_chromhmm_data.sh

```bash
$ singularity exec <container> /usr/local/bin/download_chromhmm_data.sh
$ podman run --it --rm --entrypoint /usr/local/bin/download_chromhmm_data.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download_chromhmm_data.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### funzip

```bash
$ singularity exec <container> /usr/local/bin/funzip
$ podman run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzipsfx

```bash
$ singularity exec <container> /usr/local/bin/unzipsfx
$ podman run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipgrep

```bash
$ singularity exec <container> /usr/local/bin/zipgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipinfo

```bash
$ singularity exec <container> /usr/local/bin/zipinfo
$ podman run --it --rm --entrypoint /usr/local/bin/zipinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzip

```bash
$ singularity exec <container> /usr/local/bin/unzip
$ podman run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jfr

```bash
$ singularity exec <container> /usr/local/bin/jfr
$ podman run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/local/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/local/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
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