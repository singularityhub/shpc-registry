---
layout: container
name:  "quay.io/biocontainers/gvcftools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gvcftools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gvcftools/container.yaml"
updated_at: "2024-12-15 03:54:19.614908"
latest: "0.17.0--he941832_3"
container_url: "https://biocontainers.pro/tools/gvcftools"
aliases:
 - "break_blocks"
 - "check_reference"
 - "extract_variants"
 - "gatk_to_gvcf"
 - "getBamAvgChromDepth.pl"
 - "get_called_regions"
 - "merge_variants"
 - "remove_region"
 - "set_haploid_region"
 - "trio"
 - "twins"
 - "perl5.26.2"
 - "podselect"
versions:
 - "0.17.0--he941832_3"
description: "shpc-registry automated BioContainers addition for gvcftools"
config: {"url": "https://biocontainers.pro/tools/gvcftools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gvcftools", "latest": {"0.17.0--he941832_3": "sha256:1f10cda45882f09c9d1436196c3a76f8a8943f980857a301dfd327b29b00f1d3"}, "tags": {"0.17.0--he941832_3": "sha256:1f10cda45882f09c9d1436196c3a76f8a8943f980857a301dfd327b29b00f1d3"}, "docker": "quay.io/biocontainers/gvcftools", "aliases": {"break_blocks": "/usr/local/bin/break_blocks", "check_reference": "/usr/local/bin/check_reference", "extract_variants": "/usr/local/bin/extract_variants", "gatk_to_gvcf": "/usr/local/bin/gatk_to_gvcf", "getBamAvgChromDepth.pl": "/usr/local/bin/getBamAvgChromDepth.pl", "get_called_regions": "/usr/local/bin/get_called_regions", "merge_variants": "/usr/local/bin/merge_variants", "remove_region": "/usr/local/bin/remove_region", "set_haploid_region": "/usr/local/bin/set_haploid_region", "trio": "/usr/local/bin/trio", "twins": "/usr/local/bin/twins", "perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gvcftools.
shpc-registry automated BioContainers addition for gvcftools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gvcftools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gvcftools:0.17.0--he941832_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gvcftools/0.17.0--he941832_3
$ module help quay.io/biocontainers/gvcftools/0.17.0--he941832_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gvcftools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gvcftools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gvcftools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gvcftools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gvcftools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gvcftools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### break_blocks

```bash
$ singularity exec <container> /usr/local/bin/break_blocks
$ podman run --it --rm --entrypoint /usr/local/bin/break_blocks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/break_blocks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_reference

```bash
$ singularity exec <container> /usr/local/bin/check_reference
$ podman run --it --rm --entrypoint /usr/local/bin/check_reference   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_reference   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_variants

```bash
$ singularity exec <container> /usr/local/bin/extract_variants
$ podman run --it --rm --entrypoint /usr/local/bin/extract_variants   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_variants   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gatk_to_gvcf

```bash
$ singularity exec <container> /usr/local/bin/gatk_to_gvcf
$ podman run --it --rm --entrypoint /usr/local/bin/gatk_to_gvcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatk_to_gvcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getBamAvgChromDepth.pl

```bash
$ singularity exec <container> /usr/local/bin/getBamAvgChromDepth.pl
$ podman run --it --rm --entrypoint /usr/local/bin/getBamAvgChromDepth.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getBamAvgChromDepth.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_called_regions

```bash
$ singularity exec <container> /usr/local/bin/get_called_regions
$ podman run --it --rm --entrypoint /usr/local/bin/get_called_regions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_called_regions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_variants

```bash
$ singularity exec <container> /usr/local/bin/merge_variants
$ podman run --it --rm --entrypoint /usr/local/bin/merge_variants   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_variants   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_region

```bash
$ singularity exec <container> /usr/local/bin/remove_region
$ podman run --it --rm --entrypoint /usr/local/bin/remove_region   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_region   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### set_haploid_region

```bash
$ singularity exec <container> /usr/local/bin/set_haploid_region
$ podman run --it --rm --entrypoint /usr/local/bin/set_haploid_region   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/set_haploid_region   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trio

```bash
$ singularity exec <container> /usr/local/bin/trio
$ podman run --it --rm --entrypoint /usr/local/bin/trio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twins

```bash
$ singularity exec <container> /usr/local/bin/twins
$ podman run --it --rm --entrypoint /usr/local/bin/twins   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twins   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.26.2

```bash
$ singularity exec <container> /usr/local/bin/perl5.26.2
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### podselect

```bash
$ singularity exec <container> /usr/local/bin/podselect
$ podman run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
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