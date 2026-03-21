---
layout: container
name:  "quay.io/biocontainers/pharmcat3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pharmcat3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pharmcat3/container.yaml"
updated_at: "2026-03-21 04:10:59.647788"
latest: "3.1.1--py312h7e72e81_0"
container_url: "https://biocontainers.pro/tools/pharmcat3"
aliases:
 - "gff2gff"
 - "jnativescan"
 - "pharmcat"
 - "pharmcat.jar"
 - "pharmcat_pipeline"
 - "pharmcat_positions.vcf.bgz"
 - "pharmcat_positions.vcf.bgz.csi"
 - "pharmcat_regions.bed"
 - "pharmcat_vcf_preprocessor"
 - "roh-viz"
 - "vrfs-variances"
 - "ref-cache"
 - "gff2gff.py"
 - "jwebserver"
 - "annot-tsv"
 - "guess-ploidy.py"
 - "plot-roh.py"
 - "run-roh.pl"
 - "jpackage"
 - "color-chrs.pl"
 - "plot-vcfstats"
 - "bcftools"
 - "vcfutils.pl"
 - "cups-config"
 - "ippeveprinter"
 - "ipptool"
 - "numpy-config"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "jfr"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
versions:
 - "3.1.1--py312h7e72e81_0"
description: "singularity registry hpc automated addition for pharmcat3"
config: {"url": "https://biocontainers.pro/tools/pharmcat3", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pharmcat3", "latest": {"3.1.1--py312h7e72e81_0": "sha256:bfec10c22409476074ac99b4f73093beec1bafb1777197c30e9582225c9d11fb"}, "tags": {"3.1.1--py312h7e72e81_0": "sha256:bfec10c22409476074ac99b4f73093beec1bafb1777197c30e9582225c9d11fb"}, "docker": "quay.io/biocontainers/pharmcat3", "aliases": {"gff2gff": "/usr/local/bin/gff2gff", "jnativescan": "/usr/local/bin/jnativescan", "pharmcat": "/usr/local/bin/pharmcat", "pharmcat.jar": "/usr/local/bin/pharmcat.jar", "pharmcat_pipeline": "/usr/local/bin/pharmcat_pipeline", "pharmcat_positions.vcf.bgz": "/usr/local/bin/pharmcat_positions.vcf.bgz", "pharmcat_positions.vcf.bgz.csi": "/usr/local/bin/pharmcat_positions.vcf.bgz.csi", "pharmcat_regions.bed": "/usr/local/bin/pharmcat_regions.bed", "pharmcat_vcf_preprocessor": "/usr/local/bin/pharmcat_vcf_preprocessor", "roh-viz": "/usr/local/bin/roh-viz", "vrfs-variances": "/usr/local/bin/vrfs-variances", "ref-cache": "/usr/local/bin/ref-cache", "gff2gff.py": "/usr/local/bin/gff2gff.py", "jwebserver": "/usr/local/bin/jwebserver", "annot-tsv": "/usr/local/bin/annot-tsv", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py", "run-roh.pl": "/usr/local/bin/run-roh.pl", "jpackage": "/usr/local/bin/jpackage", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "plot-vcfstats": "/usr/local/bin/plot-vcfstats", "bcftools": "/usr/local/bin/bcftools", "vcfutils.pl": "/usr/local/bin/vcfutils.pl", "cups-config": "/usr/local/bin/cups-config", "ippeveprinter": "/usr/local/bin/ippeveprinter", "ipptool": "/usr/local/bin/ipptool", "numpy-config": "/usr/local/bin/numpy-config", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "jfr": "/usr/local/bin/jfr", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pharmcat3.
singularity registry hpc automated addition for pharmcat3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pharmcat3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pharmcat3:3.1.1--py312h7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pharmcat3/3.1.1--py312h7e72e81_0
$ module help quay.io/biocontainers/pharmcat3/3.1.1--py312h7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pharmcat3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pharmcat3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pharmcat3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pharmcat3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pharmcat3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pharmcat3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gff2gff

```bash
$ singularity exec <container> /usr/local/bin/gff2gff
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jnativescan

```bash
$ singularity exec <container> /usr/local/bin/jnativescan
$ podman run --it --rm --entrypoint /usr/local/bin/jnativescan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jnativescan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pharmcat

```bash
$ singularity exec <container> /usr/local/bin/pharmcat
$ podman run --it --rm --entrypoint /usr/local/bin/pharmcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pharmcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pharmcat.jar

```bash
$ singularity exec <container> /usr/local/bin/pharmcat.jar
$ podman run --it --rm --entrypoint /usr/local/bin/pharmcat.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pharmcat.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pharmcat_pipeline

```bash
$ singularity exec <container> /usr/local/bin/pharmcat_pipeline
$ podman run --it --rm --entrypoint /usr/local/bin/pharmcat_pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pharmcat_pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pharmcat_positions.vcf.bgz

```bash
$ singularity exec <container> /usr/local/bin/pharmcat_positions.vcf.bgz
$ podman run --it --rm --entrypoint /usr/local/bin/pharmcat_positions.vcf.bgz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pharmcat_positions.vcf.bgz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pharmcat_positions.vcf.bgz.csi

```bash
$ singularity exec <container> /usr/local/bin/pharmcat_positions.vcf.bgz.csi
$ podman run --it --rm --entrypoint /usr/local/bin/pharmcat_positions.vcf.bgz.csi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pharmcat_positions.vcf.bgz.csi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pharmcat_regions.bed

```bash
$ singularity exec <container> /usr/local/bin/pharmcat_regions.bed
$ podman run --it --rm --entrypoint /usr/local/bin/pharmcat_regions.bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pharmcat_regions.bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pharmcat_vcf_preprocessor

```bash
$ singularity exec <container> /usr/local/bin/pharmcat_vcf_preprocessor
$ podman run --it --rm --entrypoint /usr/local/bin/pharmcat_vcf_preprocessor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pharmcat_vcf_preprocessor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roh-viz

```bash
$ singularity exec <container> /usr/local/bin/roh-viz
$ podman run --it --rm --entrypoint /usr/local/bin/roh-viz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roh-viz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vrfs-variances

```bash
$ singularity exec <container> /usr/local/bin/vrfs-variances
$ podman run --it --rm --entrypoint /usr/local/bin/vrfs-variances   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vrfs-variances   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jwebserver

```bash
$ singularity exec <container> /usr/local/bin/jwebserver
$ podman run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jpackage

```bash
$ singularity exec <container> /usr/local/bin/jpackage
$ podman run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### cups-config

```bash
$ singularity exec <container> /usr/local/bin/cups-config
$ podman run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ippeveprinter

```bash
$ singularity exec <container> /usr/local/bin/ippeveprinter
$ podman run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipptool

```bash
$ singularity exec <container> /usr/local/bin/ipptool
$ podman run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jfr

```bash
$ singularity exec <container> /usr/local/bin/jfr
$ podman run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/local/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/local/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage

```bash
$ singularity exec <container> /usr/local/bin/jimage
$ podman run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
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