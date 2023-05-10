---
layout: container
name:  "quay.io/biocontainers/python-hivclustering"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/python-hivclustering/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/python-hivclustering/container.yaml"
updated_at: "2023-05-10 03:06:12.577922"
latest: "1.5.6--py_0"
container_url: "https://biocontainers.pro/tools/python-hivclustering"
aliases:
 - "TNS"
 - "bam2fna"
 - "bam2msa"
 - "bamclip"
 - "bealign"
 - "ccache-swig"
 - "clipedge"
 - "consensus"
 - "hivnetworkannotate"
 - "hivnetworkcsv"
 - "msa2bam"
 - "seqmerge"
 - "swig"
 - "translate"
 - "f2py3.6"
 - "guess-ploidy.py"
 - "plot-roh.py"
 - "run-roh.pl"
 - "color-chrs.pl"
 - "plot-vcfstats"
 - "bcftools"
 - "vcfutils.pl"
 - "2to3-3.6"
 - "idle3.6"
versions:
 - "1.5.6--py_0"
description: "shpc-registry automated BioContainers addition for python-hivclustering"
config: {"url": "https://biocontainers.pro/tools/python-hivclustering", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for python-hivclustering", "latest": {"1.5.6--py_0": "sha256:fedc821998c05509aa791feb61bb7b213811eea027b9f34cf4475a4e48ad19cf"}, "tags": {"1.5.6--py_0": "sha256:fedc821998c05509aa791feb61bb7b213811eea027b9f34cf4475a4e48ad19cf"}, "docker": "quay.io/biocontainers/python-hivclustering", "aliases": {"TNS": "/usr/local/bin/TNS", "bam2fna": "/usr/local/bin/bam2fna", "bam2msa": "/usr/local/bin/bam2msa", "bamclip": "/usr/local/bin/bamclip", "bealign": "/usr/local/bin/bealign", "ccache-swig": "/usr/local/bin/ccache-swig", "clipedge": "/usr/local/bin/clipedge", "consensus": "/usr/local/bin/consensus", "hivnetworkannotate": "/usr/local/bin/hivnetworkannotate", "hivnetworkcsv": "/usr/local/bin/hivnetworkcsv", "msa2bam": "/usr/local/bin/msa2bam", "seqmerge": "/usr/local/bin/seqmerge", "swig": "/usr/local/bin/swig", "translate": "/usr/local/bin/translate", "f2py3.6": "/usr/local/bin/f2py3.6", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py", "run-roh.pl": "/usr/local/bin/run-roh.pl", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "plot-vcfstats": "/usr/local/bin/plot-vcfstats", "bcftools": "/usr/local/bin/bcftools", "vcfutils.pl": "/usr/local/bin/vcfutils.pl", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/python-hivclustering.
shpc-registry automated BioContainers addition for python-hivclustering
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/python-hivclustering
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/python-hivclustering:1.5.6--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/python-hivclustering/1.5.6--py_0
$ module help quay.io/biocontainers/python-hivclustering/1.5.6--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### python-hivclustering-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### python-hivclustering-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### python-hivclustering-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### python-hivclustering-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### python-hivclustering-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### python-hivclustering-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### TNS

```bash
$ singularity exec <container> /usr/local/bin/TNS
$ podman run --it --rm --entrypoint /usr/local/bin/TNS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TNS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2fna

```bash
$ singularity exec <container> /usr/local/bin/bam2fna
$ podman run --it --rm --entrypoint /usr/local/bin/bam2fna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2fna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2msa

```bash
$ singularity exec <container> /usr/local/bin/bam2msa
$ podman run --it --rm --entrypoint /usr/local/bin/bam2msa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2msa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamclip

```bash
$ singularity exec <container> /usr/local/bin/bamclip
$ podman run --it --rm --entrypoint /usr/local/bin/bamclip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamclip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bealign

```bash
$ singularity exec <container> /usr/local/bin/bealign
$ podman run --it --rm --entrypoint /usr/local/bin/bealign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bealign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccache-swig

```bash
$ singularity exec <container> /usr/local/bin/ccache-swig
$ podman run --it --rm --entrypoint /usr/local/bin/ccache-swig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccache-swig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clipedge

```bash
$ singularity exec <container> /usr/local/bin/clipedge
$ podman run --it --rm --entrypoint /usr/local/bin/clipedge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clipedge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### consensus

```bash
$ singularity exec <container> /usr/local/bin/consensus
$ podman run --it --rm --entrypoint /usr/local/bin/consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hivnetworkannotate

```bash
$ singularity exec <container> /usr/local/bin/hivnetworkannotate
$ podman run --it --rm --entrypoint /usr/local/bin/hivnetworkannotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hivnetworkannotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hivnetworkcsv

```bash
$ singularity exec <container> /usr/local/bin/hivnetworkcsv
$ podman run --it --rm --entrypoint /usr/local/bin/hivnetworkcsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hivnetworkcsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msa2bam

```bash
$ singularity exec <container> /usr/local/bin/msa2bam
$ podman run --it --rm --entrypoint /usr/local/bin/msa2bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msa2bam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqmerge

```bash
$ singularity exec <container> /usr/local/bin/seqmerge
$ podman run --it --rm --entrypoint /usr/local/bin/seqmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### swig

```bash
$ singularity exec <container> /usr/local/bin/swig
$ podman run --it --rm --entrypoint /usr/local/bin/swig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/swig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### translate

```bash
$ singularity exec <container> /usr/local/bin/translate
$ podman run --it --rm --entrypoint /usr/local/bin/translate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/translate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guess-ploidy.py

```bash
$ singularity exec <container> /usr/local/bin/guess-ploidy.py
$ podman run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-roh.py

```bash
$ singularity exec <container> /usr/local/bin/plot-roh.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-roh.pl

```bash
$ singularity exec <container> /usr/local/bin/run-roh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### color-chrs.pl

```bash
$ singularity exec <container> /usr/local/bin/color-chrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-vcfstats

```bash
$ singularity exec <container> /usr/local/bin/plot-vcfstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcftools

```bash
$ singularity exec <container> /usr/local/bin/bcftools
$ podman run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfutils.pl

```bash
$ singularity exec <container> /usr/local/bin/vcfutils.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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