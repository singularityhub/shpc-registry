---
layout: container
name:  "quay.io/biocontainers/bio_assembly_refinement"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bio_assembly_refinement/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bio_assembly_refinement/container.yaml"
updated_at: "2022-10-27 00:43:00.241480"
latest: "0.5.1--py_2"
container_url: "https://biocontainers.pro/tools/bio_assembly_refinement"
aliases:
 - "contig_break_finder"
 - "contig_cleaner"
 - "contig_overlap_trimmer"
 - "pacbio_post_process"
versions:
 - "0.5.1--py_2"
description: "shpc-registry automated BioContainers addition for bio_assembly_refinement"
config: {"url": "https://biocontainers.pro/tools/bio_assembly_refinement", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bio_assembly_refinement", "latest": {"0.5.1--py_2": "sha256:cecdd5aadb12c2c7f41a84e3fab2a34321989249ac303b7917b52f56124524dc"}, "tags": {"0.5.1--py_2": "sha256:cecdd5aadb12c2c7f41a84e3fab2a34321989249ac303b7917b52f56124524dc"}, "docker": "quay.io/biocontainers/bio_assembly_refinement", "aliases": {"contig_break_finder": "/usr/local/bin/contig_break_finder", "contig_cleaner": "/usr/local/bin/contig_cleaner", "contig_overlap_trimmer": "/usr/local/bin/contig_overlap_trimmer", "pacbio_post_process": "/usr/local/bin/pacbio_post_process"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bio_assembly_refinement.
shpc-registry automated BioContainers addition for bio_assembly_refinement
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bio_assembly_refinement
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bio_assembly_refinement:0.5.1--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bio_assembly_refinement/0.5.1--py_2
$ module help quay.io/biocontainers/bio_assembly_refinement/0.5.1--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bio_assembly_refinement-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bio_assembly_refinement-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bio_assembly_refinement-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bio_assembly_refinement-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bio_assembly_refinement-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bio_assembly_refinement-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### contig_break_finder

```bash
$ singularity exec <container> /usr/local/bin/contig_break_finder
$ podman run --it --rm --entrypoint /usr/local/bin/contig_break_finder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contig_break_finder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contig_cleaner

```bash
$ singularity exec <container> /usr/local/bin/contig_cleaner
$ podman run --it --rm --entrypoint /usr/local/bin/contig_cleaner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contig_cleaner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contig_overlap_trimmer

```bash
$ singularity exec <container> /usr/local/bin/contig_overlap_trimmer
$ podman run --it --rm --entrypoint /usr/local/bin/contig_overlap_trimmer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contig_overlap_trimmer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pacbio_post_process

```bash
$ singularity exec <container> /usr/local/bin/pacbio_post_process
$ podman run --it --rm --entrypoint /usr/local/bin/pacbio_post_process   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pacbio_post_process   -v ${PWD} -w ${PWD} <container> -c " $@"
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