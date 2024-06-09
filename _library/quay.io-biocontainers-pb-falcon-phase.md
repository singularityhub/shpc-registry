---
layout: container
name:  "quay.io/biocontainers/pb-falcon-phase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pb-falcon-phase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pb-falcon-phase/container.yaml"
updated_at: "2024-06-09 03:17:51.009604"
latest: "0.1.0--h5aa19ff_3"
container_url: "https://biocontainers.pro/tools/pb-falcon-phase"
aliases:
 - "FALCON_headerConverter.pl"
 - "falcon-phase"
 - "fc_primary_contig_index.pl"
 - "fc_scrub_names.pl"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.1.0--h5aa19ff_3"
description: "shpc-registry automated BioContainers addition for pb-falcon-phase"
config: {"url": "https://biocontainers.pro/tools/pb-falcon-phase", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pb-falcon-phase", "latest": {"0.1.0--h5aa19ff_3": "sha256:639f2048ffd44ef1abeeb360d2601c0a707fb592e3a2d4911e3b5270fc82dc3d"}, "tags": {"0.1.0--h5aa19ff_3": "sha256:639f2048ffd44ef1abeeb360d2601c0a707fb592e3a2d4911e3b5270fc82dc3d"}, "docker": "quay.io/biocontainers/pb-falcon-phase", "aliases": {"FALCON_headerConverter.pl": "/usr/local/bin/FALCON_headerConverter.pl", "falcon-phase": "/usr/local/bin/falcon-phase", "fc_primary_contig_index.pl": "/usr/local/bin/fc_primary_contig_index.pl", "fc_scrub_names.pl": "/usr/local/bin/fc_scrub_names.pl", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pb-falcon-phase.
shpc-registry automated BioContainers addition for pb-falcon-phase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pb-falcon-phase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pb-falcon-phase:0.1.0--h5aa19ff_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pb-falcon-phase/0.1.0--h5aa19ff_3
$ module help quay.io/biocontainers/pb-falcon-phase/0.1.0--h5aa19ff_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pb-falcon-phase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pb-falcon-phase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pb-falcon-phase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pb-falcon-phase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pb-falcon-phase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pb-falcon-phase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FALCON_headerConverter.pl

```bash
$ singularity exec <container> /usr/local/bin/FALCON_headerConverter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/FALCON_headerConverter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FALCON_headerConverter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### falcon-phase

```bash
$ singularity exec <container> /usr/local/bin/falcon-phase
$ podman run --it --rm --entrypoint /usr/local/bin/falcon-phase   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/falcon-phase   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc_primary_contig_index.pl

```bash
$ singularity exec <container> /usr/local/bin/fc_primary_contig_index.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fc_primary_contig_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc_primary_contig_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc_scrub_names.pl

```bash
$ singularity exec <container> /usr/local/bin/fc_scrub_names.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fc_scrub_names.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc_scrub_names.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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