---
layout: container
name:  "quay.io/biocontainers/asgal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/asgal/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/asgal/container.yaml"
updated_at: "2023-05-03 03:13:12.432113"
latest: "1.1.8--h5b5514e_0"
container_url: "https://biocontainers.pro/tools/asgal"
aliases:
 - "SpliceAwareAligner"
 - "asgal"
 - "asgal_BitVector.py"
 - "asgal_SplicingGraph.py"
 - "asgal_detectEvents.py"
 - "asgal_formatSAM.py"
 - "asgal_utils.py"
 - "dimacs-solver"
 - "dimacs-to-lgf"
 - "lemon-0.x-to-1.x.sh"
 - "lgf-gen"
 - "salmon"
 - "gffutils-cli"
 - "cbc"
 - "clp"
 - "vcf_sample_filter.py"
 - "vcf_filter.py"
 - "vcf_melt"
 - "faidx"
 - "glpsol"
 - "activate-global-python-argcomplete"
 - "python-argcomplete-check-easy-install-script"
 - "python-argcomplete-tcsh"
 - "register-python-argcomplete"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "f2py3.10"
 - "ace2sam"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "export2sam.pl"
 - "interpolate_sam.pl"
 - "maq2sam-long"
 - "maq2sam-short"
 - "md5fa"
 - "md5sum-lite"
versions:
 - "1.1.8--h5b5514e_0"
description: "singularity registry hpc automated addition for asgal"
config: {"url": "https://biocontainers.pro/tools/asgal", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for asgal", "latest": {"1.1.8--h5b5514e_0": "sha256:7f7955668f615a790a5bad0439a71382596f54eef59dc3dd97cd2ae010d36455"}, "tags": {"1.1.8--h5b5514e_0": "sha256:7f7955668f615a790a5bad0439a71382596f54eef59dc3dd97cd2ae010d36455"}, "docker": "quay.io/biocontainers/asgal", "aliases": {"SpliceAwareAligner": "/usr/local/bin/SpliceAwareAligner", "asgal": "/usr/local/bin/asgal", "asgal_BitVector.py": "/usr/local/bin/asgal_BitVector.py", "asgal_SplicingGraph.py": "/usr/local/bin/asgal_SplicingGraph.py", "asgal_detectEvents.py": "/usr/local/bin/asgal_detectEvents.py", "asgal_formatSAM.py": "/usr/local/bin/asgal_formatSAM.py", "asgal_utils.py": "/usr/local/bin/asgal_utils.py", "dimacs-solver": "/usr/local/bin/dimacs-solver", "dimacs-to-lgf": "/usr/local/bin/dimacs-to-lgf", "lemon-0.x-to-1.x.sh": "/usr/local/bin/lemon-0.x-to-1.x.sh", "lgf-gen": "/usr/local/bin/lgf-gen", "salmon": "/usr/local/bin/salmon", "gffutils-cli": "/usr/local/bin/gffutils-cli", "cbc": "/usr/local/bin/cbc", "clp": "/usr/local/bin/clp", "vcf_sample_filter.py": "/usr/local/bin/vcf_sample_filter.py", "vcf_filter.py": "/usr/local/bin/vcf_filter.py", "vcf_melt": "/usr/local/bin/vcf_melt", "faidx": "/usr/local/bin/faidx", "glpsol": "/usr/local/bin/glpsol", "activate-global-python-argcomplete": "/usr/local/bin/activate-global-python-argcomplete", "python-argcomplete-check-easy-install-script": "/usr/local/bin/python-argcomplete-check-easy-install-script", "python-argcomplete-tcsh": "/usr/local/bin/python-argcomplete-tcsh", "register-python-argcomplete": "/usr/local/bin/register-python-argcomplete", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "f2py3.10": "/usr/local/bin/f2py3.10", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl", "interpolate_sam.pl": "/usr/local/bin/interpolate_sam.pl", "maq2sam-long": "/usr/local/bin/maq2sam-long", "maq2sam-short": "/usr/local/bin/maq2sam-short", "md5fa": "/usr/local/bin/md5fa", "md5sum-lite": "/usr/local/bin/md5sum-lite"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/asgal.
singularity registry hpc automated addition for asgal
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/asgal
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/asgal:1.1.8--h5b5514e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/asgal/1.1.8--h5b5514e_0
$ module help quay.io/biocontainers/asgal/1.1.8--h5b5514e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### asgal-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### asgal-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### asgal-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### asgal-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### asgal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### asgal-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SpliceAwareAligner

```bash
$ singularity exec <container> /usr/local/bin/SpliceAwareAligner
$ podman run --it --rm --entrypoint /usr/local/bin/SpliceAwareAligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SpliceAwareAligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asgal

```bash
$ singularity exec <container> /usr/local/bin/asgal
$ podman run --it --rm --entrypoint /usr/local/bin/asgal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asgal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asgal_BitVector.py

```bash
$ singularity exec <container> /usr/local/bin/asgal_BitVector.py
$ podman run --it --rm --entrypoint /usr/local/bin/asgal_BitVector.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asgal_BitVector.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asgal_SplicingGraph.py

```bash
$ singularity exec <container> /usr/local/bin/asgal_SplicingGraph.py
$ podman run --it --rm --entrypoint /usr/local/bin/asgal_SplicingGraph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asgal_SplicingGraph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asgal_detectEvents.py

```bash
$ singularity exec <container> /usr/local/bin/asgal_detectEvents.py
$ podman run --it --rm --entrypoint /usr/local/bin/asgal_detectEvents.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asgal_detectEvents.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asgal_formatSAM.py

```bash
$ singularity exec <container> /usr/local/bin/asgal_formatSAM.py
$ podman run --it --rm --entrypoint /usr/local/bin/asgal_formatSAM.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asgal_formatSAM.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asgal_utils.py

```bash
$ singularity exec <container> /usr/local/bin/asgal_utils.py
$ podman run --it --rm --entrypoint /usr/local/bin/asgal_utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asgal_utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dimacs-solver

```bash
$ singularity exec <container> /usr/local/bin/dimacs-solver
$ podman run --it --rm --entrypoint /usr/local/bin/dimacs-solver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dimacs-solver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dimacs-to-lgf

```bash
$ singularity exec <container> /usr/local/bin/dimacs-to-lgf
$ podman run --it --rm --entrypoint /usr/local/bin/dimacs-to-lgf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dimacs-to-lgf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lemon-0.x-to-1.x.sh

```bash
$ singularity exec <container> /usr/local/bin/lemon-0.x-to-1.x.sh
$ podman run --it --rm --entrypoint /usr/local/bin/lemon-0.x-to-1.x.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lemon-0.x-to-1.x.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lgf-gen

```bash
$ singularity exec <container> /usr/local/bin/lgf-gen
$ podman run --it --rm --entrypoint /usr/local/bin/lgf-gen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lgf-gen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### salmon

```bash
$ singularity exec <container> /usr/local/bin/salmon
$ podman run --it --rm --entrypoint /usr/local/bin/salmon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/salmon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffutils-cli

```bash
$ singularity exec <container> /usr/local/bin/gffutils-cli
$ podman run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbc

```bash
$ singularity exec <container> /usr/local/bin/cbc
$ podman run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clp

```bash
$ singularity exec <container> /usr/local/bin/clp
$ podman run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_sample_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_sample_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_melt

```bash
$ singularity exec <container> /usr/local/bin/vcf_melt
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faidx

```bash
$ singularity exec <container> /usr/local/bin/faidx
$ podman run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### activate-global-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/activate-global-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-check-easy-install-script

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-check-easy-install-script
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-tcsh

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-tcsh
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### register-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/register-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/bowtie2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### export2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/export2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interpolate_sam.pl

```bash
$ singularity exec <container> /usr/local/bin/interpolate_sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maq2sam-long

```bash
$ singularity exec <container> /usr/local/bin/maq2sam-long
$ podman run --it --rm --entrypoint /usr/local/bin/maq2sam-long   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maq2sam-long   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maq2sam-short

```bash
$ singularity exec <container> /usr/local/bin/maq2sam-short
$ podman run --it --rm --entrypoint /usr/local/bin/maq2sam-short   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maq2sam-short   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### md5fa

```bash
$ singularity exec <container> /usr/local/bin/md5fa
$ podman run --it --rm --entrypoint /usr/local/bin/md5fa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/md5fa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### md5sum-lite

```bash
$ singularity exec <container> /usr/local/bin/md5sum-lite
$ podman run --it --rm --entrypoint /usr/local/bin/md5sum-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/md5sum-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
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