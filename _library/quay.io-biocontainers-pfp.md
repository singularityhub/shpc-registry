---
layout: container
name:  "quay.io/biocontainers/pfp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pfp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pfp/container.yaml"
updated_at: "2025-07-28 04:14:44.032163"
latest: "0.3.9--hdcf5f25_1"
container_url: "https://biocontainers.pro/tools/pfp"
aliases:
 - "check"
 - "check64"
 - "exprop"
 - "exprop64"
 - "mpfp++"
 - "mpfp++64"
 - "pfp++"
 - "pfp++64"
 - "vcf_to_fa"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.3.8--h867801b_0"
 - "0.3.8--hd36ca80_1"
 - "0.3.8--h146fbdb_2"
 - "0.3.9--h146fbdb_0"
 - "0.3.9--hdcf5f25_1"
description: "singularity registry hpc automated addition for pfp"
config: {"url": "https://biocontainers.pro/tools/pfp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pfp", "latest": {"0.3.9--hdcf5f25_1": "sha256:76d550b3786b1c50b79a89b6df0febfed859bf11d4a907c0addad968fa9dc4e6"}, "tags": {"0.3.8--h867801b_0": "sha256:20c5c6f68e6389a494c0eb9a97686e77d0eb2b5b61905dddb6b290b20a7cbd3a", "0.3.8--hd36ca80_1": "sha256:cf5b34c219dca7d4f298a755baaa0c367f5556df8d41e4f6ef27138d845d716c", "0.3.8--h146fbdb_2": "sha256:4da9d05413f199122622f7d3c3e699725d98ba5decffa2ba70ee1d465e4d4bf0", "0.3.9--h146fbdb_0": "sha256:b013a21ea77dee8e0a934446fe67493221290607901d3802fca38e60e7e92f2b", "0.3.9--hdcf5f25_1": "sha256:76d550b3786b1c50b79a89b6df0febfed859bf11d4a907c0addad968fa9dc4e6"}, "docker": "quay.io/biocontainers/pfp", "aliases": {"check": "/usr/local/bin/check", "check64": "/usr/local/bin/check64", "exprop": "/usr/local/bin/exprop", "exprop64": "/usr/local/bin/exprop64", "mpfp++": "/usr/local/bin/mpfp++", "mpfp++64": "/usr/local/bin/mpfp++64", "pfp++": "/usr/local/bin/pfp++", "pfp++64": "/usr/local/bin/pfp++64", "vcf_to_fa": "/usr/local/bin/vcf_to_fa", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pfp.
singularity registry hpc automated addition for pfp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pfp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pfp:0.3.9--hdcf5f25_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pfp/0.3.9--hdcf5f25_1
$ module help quay.io/biocontainers/pfp/0.3.9--hdcf5f25_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pfp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pfp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pfp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pfp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pfp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pfp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### check

```bash
$ singularity exec <container> /usr/local/bin/check
$ podman run --it --rm --entrypoint /usr/local/bin/check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check64

```bash
$ singularity exec <container> /usr/local/bin/check64
$ podman run --it --rm --entrypoint /usr/local/bin/check64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exprop

```bash
$ singularity exec <container> /usr/local/bin/exprop
$ podman run --it --rm --entrypoint /usr/local/bin/exprop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exprop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exprop64

```bash
$ singularity exec <container> /usr/local/bin/exprop64
$ podman run --it --rm --entrypoint /usr/local/bin/exprop64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exprop64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpfp++

```bash
$ singularity exec <container> /usr/local/bin/mpfp++
$ podman run --it --rm --entrypoint /usr/local/bin/mpfp++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpfp++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpfp++64

```bash
$ singularity exec <container> /usr/local/bin/mpfp++64
$ podman run --it --rm --entrypoint /usr/local/bin/mpfp++64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpfp++64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfp++

```bash
$ singularity exec <container> /usr/local/bin/pfp++
$ podman run --it --rm --entrypoint /usr/local/bin/pfp++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfp++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfp++64

```bash
$ singularity exec <container> /usr/local/bin/pfp++64
$ podman run --it --rm --entrypoint /usr/local/bin/pfp++64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfp++64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_to_fa

```bash
$ singularity exec <container> /usr/local/bin/vcf_to_fa
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_to_fa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_to_fa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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