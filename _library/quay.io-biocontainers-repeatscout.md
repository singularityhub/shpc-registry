---
layout: container
name:  "quay.io/biocontainers/repeatscout"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/repeatscout/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/repeatscout/container.yaml"
updated_at: "2023-11-19 02:32:13.163965"
latest: "1.0.6--hec16e2b_3"
container_url: "https://biocontainers.pro/tools/repeatscout"
aliases:
 - "RepeatScout"
 - "build_lmer_table"
 - "compare-out-to-gff.prl"
 - "filter-stage-1.prl"
 - "filter-stage-2.prl"
 - "merge-lmer-tables.prl"
 - "nmerge"
 - "nseg"
 - "trf4.10.0-rc.2.linux64.exe"
 - "trf"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.0.6--hec16e2b_3"
description: "shpc-registry automated BioContainers addition for repeatscout"
config: {"url": "https://biocontainers.pro/tools/repeatscout", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for repeatscout", "latest": {"1.0.6--hec16e2b_3": "sha256:6452aef972e37b3be9f7c1fe321c53c73ac7d61d98e3dd116039cc8218777694"}, "tags": {"1.0.6--hec16e2b_3": "sha256:6452aef972e37b3be9f7c1fe321c53c73ac7d61d98e3dd116039cc8218777694"}, "docker": "quay.io/biocontainers/repeatscout", "aliases": {"RepeatScout": "/usr/local/bin/RepeatScout", "build_lmer_table": "/usr/local/bin/build_lmer_table", "compare-out-to-gff.prl": "/usr/local/bin/compare-out-to-gff.prl", "filter-stage-1.prl": "/usr/local/bin/filter-stage-1.prl", "filter-stage-2.prl": "/usr/local/bin/filter-stage-2.prl", "merge-lmer-tables.prl": "/usr/local/bin/merge-lmer-tables.prl", "nmerge": "/usr/local/bin/nmerge", "nseg": "/usr/local/bin/nseg", "trf4.10.0-rc.2.linux64.exe": "/usr/local/bin/trf4.10.0-rc.2.linux64.exe", "trf": "/usr/local/bin/trf", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/repeatscout.
shpc-registry automated BioContainers addition for repeatscout
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/repeatscout
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/repeatscout:1.0.6--hec16e2b_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/repeatscout/1.0.6--hec16e2b_3
$ module help quay.io/biocontainers/repeatscout/1.0.6--hec16e2b_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### repeatscout-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### repeatscout-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### repeatscout-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### repeatscout-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### repeatscout-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### repeatscout-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RepeatScout

```bash
$ singularity exec <container> /usr/local/bin/RepeatScout
$ podman run --it --rm --entrypoint /usr/local/bin/RepeatScout   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RepeatScout   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_lmer_table

```bash
$ singularity exec <container> /usr/local/bin/build_lmer_table
$ podman run --it --rm --entrypoint /usr/local/bin/build_lmer_table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_lmer_table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare-out-to-gff.prl

```bash
$ singularity exec <container> /usr/local/bin/compare-out-to-gff.prl
$ podman run --it --rm --entrypoint /usr/local/bin/compare-out-to-gff.prl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare-out-to-gff.prl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-stage-1.prl

```bash
$ singularity exec <container> /usr/local/bin/filter-stage-1.prl
$ podman run --it --rm --entrypoint /usr/local/bin/filter-stage-1.prl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-stage-1.prl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-stage-2.prl

```bash
$ singularity exec <container> /usr/local/bin/filter-stage-2.prl
$ podman run --it --rm --entrypoint /usr/local/bin/filter-stage-2.prl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-stage-2.prl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge-lmer-tables.prl

```bash
$ singularity exec <container> /usr/local/bin/merge-lmer-tables.prl
$ podman run --it --rm --entrypoint /usr/local/bin/merge-lmer-tables.prl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-lmer-tables.prl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nmerge

```bash
$ singularity exec <container> /usr/local/bin/nmerge
$ podman run --it --rm --entrypoint /usr/local/bin/nmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nseg

```bash
$ singularity exec <container> /usr/local/bin/nseg
$ podman run --it --rm --entrypoint /usr/local/bin/nseg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nseg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trf4.10.0-rc.2.linux64.exe

```bash
$ singularity exec <container> /usr/local/bin/trf4.10.0-rc.2.linux64.exe
$ podman run --it --rm --entrypoint /usr/local/bin/trf4.10.0-rc.2.linux64.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trf4.10.0-rc.2.linux64.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trf

```bash
$ singularity exec <container> /usr/local/bin/trf
$ podman run --it --rm --entrypoint /usr/local/bin/trf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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