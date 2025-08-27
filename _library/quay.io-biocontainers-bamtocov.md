---
layout: container
name:  "quay.io/biocontainers/bamtocov"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bamtocov/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bamtocov/container.yaml"
updated_at: "2025-08-27 03:34:53.504610"
latest: "2.7.0--h6ead514_2"
container_url: "https://biocontainers.pro/tools/bamtocov"
aliases:
 - "average-coverage.py"
 - "bamcountrefs"
 - "bamtarget"
 - "bamtocounts"
 - "bamtocov"
 - "comparecounts.py"
 - "covToWig.py"
 - "covtotarget"
 - "feat-counts.py"
 - "gff2bed.py"
 - "low-cov-multisample.py"
 - "make-target-from-bam.py"
 - "prokka-annotation-refupdate.py"
 - "strip-seq-from-bam.py"
 - "gff2bed"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "2.7.0--hbd632db_1"
 - "2.7.0--h6ead514_2"
description: "shpc-registry automated BioContainers addition for bamtocov"
config: {"url": "https://biocontainers.pro/tools/bamtocov", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bamtocov", "latest": {"2.7.0--h6ead514_2": "sha256:1afe525fc47c74c94e1588ebf5fb64a1ba0c3087b04cf86f6b3b56bb32224099"}, "tags": {"2.7.0--hbd632db_1": "sha256:adaf35c67d230809d289ee9efee15906fbcb62b9e39c3aadb631e70e54f648d8", "2.7.0--h6ead514_2": "sha256:1afe525fc47c74c94e1588ebf5fb64a1ba0c3087b04cf86f6b3b56bb32224099"}, "docker": "quay.io/biocontainers/bamtocov", "aliases": {"average-coverage.py": "/usr/local/bin/average-coverage.py", "bamcountrefs": "/usr/local/bin/bamcountrefs", "bamtarget": "/usr/local/bin/bamtarget", "bamtocounts": "/usr/local/bin/bamtocounts", "bamtocov": "/usr/local/bin/bamtocov", "comparecounts.py": "/usr/local/bin/comparecounts.py", "covToWig.py": "/usr/local/bin/covToWig.py", "covtotarget": "/usr/local/bin/covtotarget", "feat-counts.py": "/usr/local/bin/feat-counts.py", "gff2bed.py": "/usr/local/bin/gff2bed.py", "low-cov-multisample.py": "/usr/local/bin/low-cov-multisample.py", "make-target-from-bam.py": "/usr/local/bin/make-target-from-bam.py", "prokka-annotation-refupdate.py": "/usr/local/bin/prokka-annotation-refupdate.py", "strip-seq-from-bam.py": "/usr/local/bin/strip-seq-from-bam.py", "gff2bed": "/usr/local/bin/gff2bed", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bamtocov.
shpc-registry automated BioContainers addition for bamtocov
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bamtocov
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bamtocov:2.7.0--h6ead514_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bamtocov/2.7.0--h6ead514_2
$ module help quay.io/biocontainers/bamtocov/2.7.0--h6ead514_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bamtocov-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bamtocov-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bamtocov-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bamtocov-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bamtocov-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bamtocov-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### average-coverage.py

```bash
$ singularity exec <container> /usr/local/bin/average-coverage.py
$ podman run --it --rm --entrypoint /usr/local/bin/average-coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/average-coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamcountrefs

```bash
$ singularity exec <container> /usr/local/bin/bamcountrefs
$ podman run --it --rm --entrypoint /usr/local/bin/bamcountrefs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamcountrefs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtarget

```bash
$ singularity exec <container> /usr/local/bin/bamtarget
$ podman run --it --rm --entrypoint /usr/local/bin/bamtarget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtarget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtocounts

```bash
$ singularity exec <container> /usr/local/bin/bamtocounts
$ podman run --it --rm --entrypoint /usr/local/bin/bamtocounts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtocounts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtocov

```bash
$ singularity exec <container> /usr/local/bin/bamtocov
$ podman run --it --rm --entrypoint /usr/local/bin/bamtocov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtocov   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### comparecounts.py

```bash
$ singularity exec <container> /usr/local/bin/comparecounts.py
$ podman run --it --rm --entrypoint /usr/local/bin/comparecounts.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/comparecounts.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### covToWig.py

```bash
$ singularity exec <container> /usr/local/bin/covToWig.py
$ podman run --it --rm --entrypoint /usr/local/bin/covToWig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/covToWig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### covtotarget

```bash
$ singularity exec <container> /usr/local/bin/covtotarget
$ podman run --it --rm --entrypoint /usr/local/bin/covtotarget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/covtotarget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### feat-counts.py

```bash
$ singularity exec <container> /usr/local/bin/feat-counts.py
$ podman run --it --rm --entrypoint /usr/local/bin/feat-counts.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/feat-counts.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2bed.py

```bash
$ singularity exec <container> /usr/local/bin/gff2bed.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### low-cov-multisample.py

```bash
$ singularity exec <container> /usr/local/bin/low-cov-multisample.py
$ podman run --it --rm --entrypoint /usr/local/bin/low-cov-multisample.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/low-cov-multisample.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make-target-from-bam.py

```bash
$ singularity exec <container> /usr/local/bin/make-target-from-bam.py
$ podman run --it --rm --entrypoint /usr/local/bin/make-target-from-bam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make-target-from-bam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-annotation-refupdate.py

```bash
$ singularity exec <container> /usr/local/bin/prokka-annotation-refupdate.py
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-annotation-refupdate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-annotation-refupdate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strip-seq-from-bam.py

```bash
$ singularity exec <container> /usr/local/bin/strip-seq-from-bam.py
$ podman run --it --rm --entrypoint /usr/local/bin/strip-seq-from-bam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strip-seq-from-bam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2bed

```bash
$ singularity exec <container> /usr/local/bin/gff2bed
$ podman run --it --rm --entrypoint /usr/local/bin/gff2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
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