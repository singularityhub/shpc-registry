---
layout: container
name:  "quay.io/biocontainers/bedops"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bedops/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bedops/container.yaml"
updated_at: "2022-10-27 00:41:12.235605"
latest: "2.4.23--0"
container_url: "https://singularity-hpc.readthedocs.io"
aliases:
 - "bam2bed"
 - "bam2bed_gnuParallel"
 - "bam2bed_sge"
 - "bam2bed_slurm"
 - "bam2starch"
 - "bam2starch_gnuParallel"
 - "bam2starch_sge"
 - "bam2starch_slurm"
 - "bedextract"
 - "bedmap"
 - "bedops"
 - "closest-features"
 - "conda"
 - "convert2bed"
 - "deactivate"
 - "gff2bed"
 - "gff2starch"
 - "gtf2bed"
 - "gtf2starch"
 - "gvf2bed"
 - "gvf2starch"
 - "psl2bed"
 - "psl2starch"
 - "rmsk2bed"
 - "rmsk2starch"
 - "sam2bed"
 - "sam2starch"
 - "sort-bed"
 - "starch"
 - "starchcat"
 - "starchcluster_gnuParallel"
 - "starchcluster_sge"
 - "starchcluster_slurm"
 - "unstarch"
 - "vcf2bed"
 - "vcf2starch"
 - "wig2bed"
 - "wig2starch"
versions:
 - "2.4.23--0"
description: "Efficient and scalable boolean and other set operations for genomic data."
config: {"url": "https://singularity-hpc.readthedocs.io", "maintainer": "vsoch", "description": "Efficient and scalable boolean and other set operations for genomic data.", "latest": {"2.4.23--0": "sha256:fd8d19a1eee1702ceb9e16a224974143c4e99a62c3c39e05e67d1827b0046ff7"}, "tags": {"2.4.23--0": "sha256:fd8d19a1eee1702ceb9e16a224974143c4e99a62c3c39e05e67d1827b0046ff7"}, "docker": "quay.io/biocontainers/bedops", "aliases": {"bam2bed": "/usr/local/bin/bam2bed", "bam2bed_gnuParallel": "/usr/local/bin/bam2bed_gnuParallel", "bam2bed_sge": "/usr/local/bin/bam2bed_sge", "bam2bed_slurm": "/usr/local/bin/bam2bed_slurm", "bam2starch": "/usr/local/bin/bam2starch", "bam2starch_gnuParallel": "/usr/local/bin/bam2starch_gnuParallel", "bam2starch_sge": "/usr/local/bin/bam2starch_sge", "bam2starch_slurm": "/usr/local/bin/bam2starch_slurm", "bedextract": "/usr/local/bin/bedextract", "bedmap": "/usr/local/bin/bedmap", "bedops": "/usr/local/bin/bedops", "closest-features": "/usr/local/bin/closest-features", "conda": "/usr/local/bin/conda", "convert2bed": "/usr/local/bin/convert2bed", "deactivate": "/usr/local/bin/deactivate", "gff2bed": "/usr/local/bin/gff2bed", "gff2starch": "/usr/local/bin/gff2starch", "gtf2bed": "/usr/local/bin/gtf2bed", "gtf2starch": "/usr/local/bin/gtf2starch", "gvf2bed": "/usr/local/bin/gvf2bed", "gvf2starch": "/usr/local/bin/gvf2starch", "psl2bed": "/usr/local/bin/psl2bed", "psl2starch": "/usr/local/bin/psl2starch", "rmsk2bed": "/usr/local/bin/rmsk2bed", "rmsk2starch": "/usr/local/bin/rmsk2starch", "sam2bed": "/usr/local/bin/sam2bed", "sam2starch": "/usr/local/bin/sam2starch", "sort-bed": "/usr/local/bin/sort-bed", "starch": "/usr/local/bin/starch", "starchcat": "/usr/local/bin/starchcat", "starchcluster_gnuParallel": "/usr/local/bin/starchcluster_gnuParallel", "starchcluster_sge": "/usr/local/bin/starchcluster_sge", "starchcluster_slurm": "/usr/local/bin/starchcluster_slurm", "unstarch": "/usr/local/bin/unstarch", "vcf2bed": "/usr/local/bin/vcf2bed", "vcf2starch": "/usr/local/bin/vcf2starch", "wig2bed": "/usr/local/bin/wig2bed", "wig2starch": "/usr/local/bin/wig2starch"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bedops.
Efficient and scalable boolean and other set operations for genomic data.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bedops
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bedops:2.4.23--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bedops/2.4.23--0
$ module help quay.io/biocontainers/bedops/2.4.23--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bedops-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bedops-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bedops-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bedops-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bedops-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bedops-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bam2bed

```bash
$ singularity exec <container> /usr/local/bin/bam2bed
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_gnuParallel

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_gnuParallel
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_sge

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_sge
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_slurm

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_slurm
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_slurm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_slurm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2starch

```bash
$ singularity exec <container> /usr/local/bin/bam2starch
$ podman run --it --rm --entrypoint /usr/local/bin/bam2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2starch_gnuParallel

```bash
$ singularity exec <container> /usr/local/bin/bam2starch_gnuParallel
$ podman run --it --rm --entrypoint /usr/local/bin/bam2starch_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2starch_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2starch_sge

```bash
$ singularity exec <container> /usr/local/bin/bam2starch_sge
$ podman run --it --rm --entrypoint /usr/local/bin/bam2starch_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2starch_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2starch_slurm

```bash
$ singularity exec <container> /usr/local/bin/bam2starch_slurm
$ podman run --it --rm --entrypoint /usr/local/bin/bam2starch_slurm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2starch_slurm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedextract

```bash
$ singularity exec <container> /usr/local/bin/bedextract
$ podman run --it --rm --entrypoint /usr/local/bin/bedextract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedextract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedmap

```bash
$ singularity exec <container> /usr/local/bin/bedmap
$ podman run --it --rm --entrypoint /usr/local/bin/bedmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedops

```bash
$ singularity exec <container> /usr/local/bin/bedops
$ podman run --it --rm --entrypoint /usr/local/bin/bedops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedops   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### closest-features

```bash
$ singularity exec <container> /usr/local/bin/closest-features
$ podman run --it --rm --entrypoint /usr/local/bin/closest-features   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/closest-features   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda

```bash
$ singularity exec <container> /usr/local/bin/conda
$ podman run --it --rm --entrypoint /usr/local/bin/conda   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert2bed

```bash
$ singularity exec <container> /usr/local/bin/convert2bed
$ podman run --it --rm --entrypoint /usr/local/bin/convert2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deactivate

```bash
$ singularity exec <container> /usr/local/bin/deactivate
$ podman run --it --rm --entrypoint /usr/local/bin/deactivate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deactivate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2bed

```bash
$ singularity exec <container> /usr/local/bin/gff2bed
$ podman run --it --rm --entrypoint /usr/local/bin/gff2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2starch

```bash
$ singularity exec <container> /usr/local/bin/gff2starch
$ podman run --it --rm --entrypoint /usr/local/bin/gff2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf2bed

```bash
$ singularity exec <container> /usr/local/bin/gtf2bed
$ podman run --it --rm --entrypoint /usr/local/bin/gtf2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf2starch

```bash
$ singularity exec <container> /usr/local/bin/gtf2starch
$ podman run --it --rm --entrypoint /usr/local/bin/gtf2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gvf2bed

```bash
$ singularity exec <container> /usr/local/bin/gvf2bed
$ podman run --it --rm --entrypoint /usr/local/bin/gvf2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gvf2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gvf2starch

```bash
$ singularity exec <container> /usr/local/bin/gvf2starch
$ podman run --it --rm --entrypoint /usr/local/bin/gvf2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gvf2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl2bed

```bash
$ singularity exec <container> /usr/local/bin/psl2bed
$ podman run --it --rm --entrypoint /usr/local/bin/psl2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl2starch

```bash
$ singularity exec <container> /usr/local/bin/psl2starch
$ podman run --it --rm --entrypoint /usr/local/bin/psl2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmsk2bed

```bash
$ singularity exec <container> /usr/local/bin/rmsk2bed
$ podman run --it --rm --entrypoint /usr/local/bin/rmsk2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmsk2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmsk2starch

```bash
$ singularity exec <container> /usr/local/bin/rmsk2starch
$ podman run --it --rm --entrypoint /usr/local/bin/rmsk2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmsk2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam2bed

```bash
$ singularity exec <container> /usr/local/bin/sam2bed
$ podman run --it --rm --entrypoint /usr/local/bin/sam2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam2starch

```bash
$ singularity exec <container> /usr/local/bin/sam2starch
$ podman run --it --rm --entrypoint /usr/local/bin/sam2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sort-bed

```bash
$ singularity exec <container> /usr/local/bin/sort-bed
$ podman run --it --rm --entrypoint /usr/local/bin/sort-bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sort-bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starch

```bash
$ singularity exec <container> /usr/local/bin/starch
$ podman run --it --rm --entrypoint /usr/local/bin/starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/starch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starchcat

```bash
$ singularity exec <container> /usr/local/bin/starchcat
$ podman run --it --rm --entrypoint /usr/local/bin/starchcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/starchcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starchcluster_gnuParallel

```bash
$ singularity exec <container> /usr/local/bin/starchcluster_gnuParallel
$ podman run --it --rm --entrypoint /usr/local/bin/starchcluster_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/starchcluster_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starchcluster_sge

```bash
$ singularity exec <container> /usr/local/bin/starchcluster_sge
$ podman run --it --rm --entrypoint /usr/local/bin/starchcluster_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/starchcluster_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starchcluster_slurm

```bash
$ singularity exec <container> /usr/local/bin/starchcluster_slurm
$ podman run --it --rm --entrypoint /usr/local/bin/starchcluster_slurm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/starchcluster_slurm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unstarch

```bash
$ singularity exec <container> /usr/local/bin/unstarch
$ podman run --it --rm --entrypoint /usr/local/bin/unstarch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unstarch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2bed

```bash
$ singularity exec <container> /usr/local/bin/vcf2bed
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2starch

```bash
$ singularity exec <container> /usr/local/bin/vcf2starch
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wig2bed

```bash
$ singularity exec <container> /usr/local/bin/wig2bed
$ podman run --it --rm --entrypoint /usr/local/bin/wig2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wig2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wig2starch

```bash
$ singularity exec <container> /usr/local/bin/wig2starch
$ podman run --it --rm --entrypoint /usr/local/bin/wig2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wig2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
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