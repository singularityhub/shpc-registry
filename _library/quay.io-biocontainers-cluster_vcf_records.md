---
layout: container
name:  "quay.io/biocontainers/cluster_vcf_records"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cluster_vcf_records/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cluster_vcf_records/container.yaml"
updated_at: "2024-11-12 03:51:38.724136"
latest: "0.13.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cluster_vcf_records"
aliases:
 - "vt"
 - "tabix++"
 - "bc"
 - "dc"
 - "fastaq"
 - "abba-baba"
 - "bFst"
 - "bed2region"
 - "bgziptabix"
 - "dumpContigsFromHeader"
versions:
 - "0.13.3--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for cluster_vcf_records"
config: {"url": "https://biocontainers.pro/tools/cluster_vcf_records", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cluster_vcf_records", "latest": {"0.13.3--pyhdfd78af_0": "sha256:70949d65a84629f2e4c9d5efe4eeaa1ca3df7b3fba80a3f28072839977d0689e"}, "tags": {"0.13.3--pyhdfd78af_0": "sha256:70949d65a84629f2e4c9d5efe4eeaa1ca3df7b3fba80a3f28072839977d0689e"}, "docker": "quay.io/biocontainers/cluster_vcf_records", "aliases": {"vt": "/usr/local/bin/vt", "tabix++": "/usr/local/bin/tabix++", "bc": "/usr/local/bin/bc", "dc": "/usr/local/bin/dc", "fastaq": "/usr/local/bin/fastaq", "abba-baba": "/usr/local/bin/abba-baba", "bFst": "/usr/local/bin/bFst", "bed2region": "/usr/local/bin/bed2region", "bgziptabix": "/usr/local/bin/bgziptabix", "dumpContigsFromHeader": "/usr/local/bin/dumpContigsFromHeader"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cluster_vcf_records.
shpc-registry automated BioContainers addition for cluster_vcf_records
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cluster_vcf_records
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cluster_vcf_records:0.13.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cluster_vcf_records/0.13.3--pyhdfd78af_0
$ module help quay.io/biocontainers/cluster_vcf_records/0.13.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cluster_vcf_records-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cluster_vcf_records-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cluster_vcf_records-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cluster_vcf_records-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cluster_vcf_records-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cluster_vcf_records-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vt

```bash
$ singularity exec <container> /usr/local/bin/vt
$ podman run --it --rm --entrypoint /usr/local/bin/vt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vt   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### fastaq

```bash
$ singularity exec <container> /usr/local/bin/fastaq
$ podman run --it --rm --entrypoint /usr/local/bin/fastaq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaq   -v ${PWD} -w ${PWD} <container> -c " $@"
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