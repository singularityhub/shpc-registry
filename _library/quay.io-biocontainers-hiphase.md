---
layout: container
name:  "quay.io/biocontainers/hiphase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hiphase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hiphase/container.yaml"
updated_at: "2026-01-02 04:05:45.382315"
latest: "1.5.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/hiphase"
aliases:
 - "hiphase"
versions:
 - "0.8.1--h9ee0642_0"
 - "0.10.0--h9ee0642_0"
 - "0.10.2--h9ee0642_0"
 - "1.0.0--h9ee0642_0"
 - "1.1.0--h9ee0642_0"
 - "1.4.0--h9ee0642_0"
 - "1.3.0--h9ee0642_0"
 - "1.2.1--h9ee0642_0"
 - "1.4.2--h9ee0642_0"
 - "1.4.4--h9ee0642_0"
 - "1.4.5--h9ee0642_0"
 - "1.5.0--h9ee0642_0"
description: "singularity registry hpc automated addition for hiphase"
config: {"url": "https://biocontainers.pro/tools/hiphase", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hiphase", "latest": {"1.5.0--h9ee0642_0": "sha256:665d4d43b01ed5d34570fb96e56e57bc49bd9e68f0da26cc9f8ea72f3176f1bb"}, "tags": {"0.8.1--h9ee0642_0": "sha256:d05bc9e2f41528acafb442044cf1d193cfd3cfb1fafbc6c5417b91f3b557b36b", "0.10.0--h9ee0642_0": "sha256:8c8259a75e02882a590c687a33d6a405f84a679beea73b13779ec5f01db25bf1", "0.10.2--h9ee0642_0": "sha256:cc8d6f61e418f8a422140b07b8921a7b96583611052e1f485ecb2c19116109b0", "1.0.0--h9ee0642_0": "sha256:a7dad8e90e1f06925003c7735ae21fec039cc8fc4c730395a3c5c26f87dc8e55", "1.1.0--h9ee0642_0": "sha256:ab98241f4ea43746ac6d1a329290fd00d271a6de0798bbb754ba967a0d1eef25", "1.4.0--h9ee0642_0": "sha256:009ab0344c1f2be5870be507f7b8e8e5a38d28fdf4d0df91a0e3e46da616a2d9", "1.3.0--h9ee0642_0": "sha256:b8c0d3f52fc57dfa6c671c73e0f6d9af3402bd42efc252f7a8a1dfe635eb2ef8", "1.2.1--h9ee0642_0": "sha256:794f86fe29fe6d0f26be7cc073f4325c00446f03403b440fb4cdee32cc0d4123", "1.4.2--h9ee0642_0": "sha256:26d12ac145b148545ca6a27b42c793f15aec97145fe3ed8bed9f5764414b8dc2", "1.4.4--h9ee0642_0": "sha256:5b87db247273e034e8a8151613c6af528bed2e9a506bbf57aaae8fed8b6dd902", "1.4.5--h9ee0642_0": "sha256:397995001d5d4d0f4967bdc8d7fb44bc99a7135825f4edbfceb9c8ee57834312", "1.5.0--h9ee0642_0": "sha256:665d4d43b01ed5d34570fb96e56e57bc49bd9e68f0da26cc9f8ea72f3176f1bb"}, "docker": "quay.io/biocontainers/hiphase", "aliases": {"hiphase": "/usr/local/bin/hiphase"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hiphase.
singularity registry hpc automated addition for hiphase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hiphase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hiphase:1.5.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hiphase/1.5.0--h9ee0642_0
$ module help quay.io/biocontainers/hiphase/1.5.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hiphase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hiphase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hiphase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hiphase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hiphase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hiphase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hiphase

```bash
$ singularity exec <container> /usr/local/bin/hiphase
$ podman run --it --rm --entrypoint /usr/local/bin/hiphase   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hiphase   -v ${PWD} -w ${PWD} <container> -c " $@"
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