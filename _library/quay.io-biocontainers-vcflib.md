---
layout: container
name:  "quay.io/biocontainers/vcflib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vcflib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vcflib/container.yaml"
updated_at: "2024-07-08 02:43:34.061601"
latest: "1.0.9--hdcf5f25_6"
container_url: "https://biocontainers.pro/tools/vcflib"
aliases:
 - "tabix++"
 - "bc"
 - "dc"
 - "abba-baba"
 - "bFst"
 - "bed2region"
 - "bgziptabix"
 - "dumpContigsFromHeader"
 - "genotypeSummary"
 - "hapLrt"
versions:
 - "1.0.3--ha04fe3b_2"
 - "1.0.3--h6b7c446_3"
 - "1.0.3--h0033a41_4"
 - "1.0.9--h146fbdb_1"
 - "1.0.9--h146fbdb_2"
 - "1.0.9--h146fbdb_4"
 - "1.0.9--hdcf5f25_5"
 - "1.0.9--hdcf5f25_6"
description: "shpc-registry automated BioContainers addition for vcflib"
config: {"url": "https://biocontainers.pro/tools/vcflib", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vcflib", "latest": {"1.0.9--hdcf5f25_6": "sha256:cf73bef002a8a75ad34dba86a2d2309a00f0f0cb1dab243973ae32ace86d96b3"}, "tags": {"1.0.3--ha04fe3b_2": "sha256:8a4583b2ebec8d8fb64e1fc28d23acbdcfaee19cd78b151501b2e0790b95b9b3", "1.0.3--h6b7c446_3": "sha256:7ff994be6c5f3b306ef9e40674b16db8c10e30040a9ba367963e06feb1dbd5b1", "1.0.3--h0033a41_4": "sha256:a24ea4a486ad7cb6f4a0aac1541eab5e4c0478168c85d16384a69ce1c3577514", "1.0.9--h146fbdb_1": "sha256:7fe51f1d6e807c39fdd69328eb7c01c18da110aeebdbc7fa7d038d86feb348c0", "1.0.9--h146fbdb_2": "sha256:79aa88170e1dcc3c3b8e0314739dd9697b93e96fd51b4b7f6116da3663980d3d", "1.0.9--h146fbdb_4": "sha256:8ba59f9180b75651600c54249dcbaf11a3a42ca9553fc8a69694dc3b1b81af4d", "1.0.9--hdcf5f25_5": "sha256:4bb8335d7c8aeb0cba2c8ed97eafe4f37f9f563e213fb5f6bc5f5a61aa7b6f1c", "1.0.9--hdcf5f25_6": "sha256:cf73bef002a8a75ad34dba86a2d2309a00f0f0cb1dab243973ae32ace86d96b3"}, "docker": "quay.io/biocontainers/vcflib", "aliases": {"tabix++": "/usr/local/bin/tabix++", "bc": "/usr/local/bin/bc", "dc": "/usr/local/bin/dc", "abba-baba": "/usr/local/bin/abba-baba", "bFst": "/usr/local/bin/bFst", "bed2region": "/usr/local/bin/bed2region", "bgziptabix": "/usr/local/bin/bgziptabix", "dumpContigsFromHeader": "/usr/local/bin/dumpContigsFromHeader", "genotypeSummary": "/usr/local/bin/genotypeSummary", "hapLrt": "/usr/local/bin/hapLrt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vcflib.
shpc-registry automated BioContainers addition for vcflib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vcflib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vcflib:1.0.9--hdcf5f25_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vcflib/1.0.9--hdcf5f25_6
$ module help quay.io/biocontainers/vcflib/1.0.9--hdcf5f25_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vcflib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vcflib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vcflib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vcflib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vcflib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vcflib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tabix++

```bash
$ singularity exec <container> /usr/local/bin/tabix++
$ podman run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bc

```bash
$ singularity exec <container> /usr/local/bin/bc
$ podman run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dc

```bash
$ singularity exec <container> /usr/local/bin/dc
$ podman run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abba-baba

```bash
$ singularity exec <container> /usr/local/bin/abba-baba
$ podman run --it --rm --entrypoint /usr/local/bin/abba-baba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abba-baba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bFst

```bash
$ singularity exec <container> /usr/local/bin/bFst
$ podman run --it --rm --entrypoint /usr/local/bin/bFst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bFst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed2region

```bash
$ singularity exec <container> /usr/local/bin/bed2region
$ podman run --it --rm --entrypoint /usr/local/bin/bed2region   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed2region   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgziptabix

```bash
$ singularity exec <container> /usr/local/bin/bgziptabix
$ podman run --it --rm --entrypoint /usr/local/bin/bgziptabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgziptabix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dumpContigsFromHeader

```bash
$ singularity exec <container> /usr/local/bin/dumpContigsFromHeader
$ podman run --it --rm --entrypoint /usr/local/bin/dumpContigsFromHeader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dumpContigsFromHeader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genotypeSummary

```bash
$ singularity exec <container> /usr/local/bin/genotypeSummary
$ podman run --it --rm --entrypoint /usr/local/bin/genotypeSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genotypeSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hapLrt

```bash
$ singularity exec <container> /usr/local/bin/hapLrt
$ podman run --it --rm --entrypoint /usr/local/bin/hapLrt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hapLrt   -v ${PWD} -w ${PWD} <container> -c " $@"
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