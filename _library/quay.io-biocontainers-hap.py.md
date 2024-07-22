---
layout: container
name:  "quay.io/biocontainers/hap.py"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hap.py/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hap.py/container.yaml"
updated_at: "2024-07-22 03:57:09.381076"
latest: "0.3.15--py27hcb73b3d_0"
container_url: "https://biocontainers.pro/tools/hap.py"
aliases:
 - "alleles"
 - "bamstats.py"
 - "blocksplit"
 - "cnx.py"
 - "dipenum"
 - "fastainfo"
 - "ftx.py"
 - "gvcf2bed"
 - "hap.py"
 - "hapcmp"
 - "hapenum"
 - "multimerge"
 - "ovc.py"
 - "pre.py"
 - "preprocess"
 - "qfy.py"
 - "quantify"
 - "roc"
 - "scmp"
 - "som.py"
 - "test_haplotypes"
 - "validatevcf"
 - "vcfhdr2json"
 - "xcmp"
 - "vcfcheck"
 - "intersection_matrix.py"
 - "intron_exon_reads.py"
 - "nosetests"
 - "pbt_plotting_example.py"
 - "peak_pie.py"
 - "pybedtools"
 - "venn_gchart.py"
 - "venn_mpl.py"
 - "annotate.py"
versions:
 - "0.3.7--py27_1"
 - "0.3.14--py27h5c5a3ab_0"
 - "0.3.15--py27hcb73b3d_0"
description: "shpc-registry automated BioContainers addition for hap.py"
config: {"url": "https://biocontainers.pro/tools/hap.py", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hap.py", "latest": {"0.3.15--py27hcb73b3d_0": "sha256:d63b963a6cb01b4830393b22369e7b91d298e4156dde353739e74e4cfa4f96d0"}, "tags": {"0.3.7--py27_1": "sha256:5be435451264bcc00f3627fd873ee866a37b4c8fa456b3e32a43e10d64bcb2ce", "0.3.14--py27h5c5a3ab_0": "sha256:d81998ec2c4ea63588a76f760a942ac5e170749617eb9d77d1fc05446d97b3e4", "0.3.15--py27hcb73b3d_0": "sha256:d63b963a6cb01b4830393b22369e7b91d298e4156dde353739e74e4cfa4f96d0"}, "docker": "quay.io/biocontainers/hap.py", "aliases": {"alleles": "/usr/local/bin/alleles", "bamstats.py": "/usr/local/bin/bamstats.py", "blocksplit": "/usr/local/bin/blocksplit", "cnx.py": "/usr/local/bin/cnx.py", "dipenum": "/usr/local/bin/dipenum", "fastainfo": "/usr/local/bin/fastainfo", "ftx.py": "/usr/local/bin/ftx.py", "gvcf2bed": "/usr/local/bin/gvcf2bed", "hap.py": "/usr/local/bin/hap.py", "hapcmp": "/usr/local/bin/hapcmp", "hapenum": "/usr/local/bin/hapenum", "multimerge": "/usr/local/bin/multimerge", "ovc.py": "/usr/local/bin/ovc.py", "pre.py": "/usr/local/bin/pre.py", "preprocess": "/usr/local/bin/preprocess", "qfy.py": "/usr/local/bin/qfy.py", "quantify": "/usr/local/bin/quantify", "roc": "/usr/local/bin/roc", "scmp": "/usr/local/bin/scmp", "som.py": "/usr/local/bin/som.py", "test_haplotypes": "/usr/local/bin/test_haplotypes", "validatevcf": "/usr/local/bin/validatevcf", "vcfhdr2json": "/usr/local/bin/vcfhdr2json", "xcmp": "/usr/local/bin/xcmp", "vcfcheck": "/usr/local/bin/vcfcheck", "intersection_matrix.py": "/usr/local/bin/intersection_matrix.py", "intron_exon_reads.py": "/usr/local/bin/intron_exon_reads.py", "nosetests": "/usr/local/bin/nosetests", "pbt_plotting_example.py": "/usr/local/bin/pbt_plotting_example.py", "peak_pie.py": "/usr/local/bin/peak_pie.py", "pybedtools": "/usr/local/bin/pybedtools", "venn_gchart.py": "/usr/local/bin/venn_gchart.py", "venn_mpl.py": "/usr/local/bin/venn_mpl.py", "annotate.py": "/usr/local/bin/annotate.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hap.py.
shpc-registry automated BioContainers addition for hap.py
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hap.py
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hap.py:0.3.15--py27hcb73b3d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hap.py/0.3.15--py27hcb73b3d_0
$ module help quay.io/biocontainers/hap.py/0.3.15--py27hcb73b3d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hap.py-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hap.py-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hap.py-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hap.py-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hap.py-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hap.py-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alleles

```bash
$ singularity exec <container> /usr/local/bin/alleles
$ podman run --it --rm --entrypoint /usr/local/bin/alleles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alleles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamstats.py

```bash
$ singularity exec <container> /usr/local/bin/bamstats.py
$ podman run --it --rm --entrypoint /usr/local/bin/bamstats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamstats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blocksplit

```bash
$ singularity exec <container> /usr/local/bin/blocksplit
$ podman run --it --rm --entrypoint /usr/local/bin/blocksplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blocksplit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cnx.py

```bash
$ singularity exec <container> /usr/local/bin/cnx.py
$ podman run --it --rm --entrypoint /usr/local/bin/cnx.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cnx.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dipenum

```bash
$ singularity exec <container> /usr/local/bin/dipenum
$ podman run --it --rm --entrypoint /usr/local/bin/dipenum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dipenum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastainfo

```bash
$ singularity exec <container> /usr/local/bin/fastainfo
$ podman run --it --rm --entrypoint /usr/local/bin/fastainfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastainfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftx.py

```bash
$ singularity exec <container> /usr/local/bin/ftx.py
$ podman run --it --rm --entrypoint /usr/local/bin/ftx.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftx.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gvcf2bed

```bash
$ singularity exec <container> /usr/local/bin/gvcf2bed
$ podman run --it --rm --entrypoint /usr/local/bin/gvcf2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gvcf2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hap.py

```bash
$ singularity exec <container> /usr/local/bin/hap.py
$ podman run --it --rm --entrypoint /usr/local/bin/hap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hapcmp

```bash
$ singularity exec <container> /usr/local/bin/hapcmp
$ podman run --it --rm --entrypoint /usr/local/bin/hapcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hapcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hapenum

```bash
$ singularity exec <container> /usr/local/bin/hapenum
$ podman run --it --rm --entrypoint /usr/local/bin/hapenum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hapenum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multimerge

```bash
$ singularity exec <container> /usr/local/bin/multimerge
$ podman run --it --rm --entrypoint /usr/local/bin/multimerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multimerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ovc.py

```bash
$ singularity exec <container> /usr/local/bin/ovc.py
$ podman run --it --rm --entrypoint /usr/local/bin/ovc.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ovc.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pre.py

```bash
$ singularity exec <container> /usr/local/bin/pre.py
$ podman run --it --rm --entrypoint /usr/local/bin/pre.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pre.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### preprocess

```bash
$ singularity exec <container> /usr/local/bin/preprocess
$ podman run --it --rm --entrypoint /usr/local/bin/preprocess   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/preprocess   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qfy.py

```bash
$ singularity exec <container> /usr/local/bin/qfy.py
$ podman run --it --rm --entrypoint /usr/local/bin/qfy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qfy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quantify

```bash
$ singularity exec <container> /usr/local/bin/quantify
$ podman run --it --rm --entrypoint /usr/local/bin/quantify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quantify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roc

```bash
$ singularity exec <container> /usr/local/bin/roc
$ podman run --it --rm --entrypoint /usr/local/bin/roc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scmp

```bash
$ singularity exec <container> /usr/local/bin/scmp
$ podman run --it --rm --entrypoint /usr/local/bin/scmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### som.py

```bash
$ singularity exec <container> /usr/local/bin/som.py
$ podman run --it --rm --entrypoint /usr/local/bin/som.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/som.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_haplotypes

```bash
$ singularity exec <container> /usr/local/bin/test_haplotypes
$ podman run --it --rm --entrypoint /usr/local/bin/test_haplotypes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_haplotypes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### validatevcf

```bash
$ singularity exec <container> /usr/local/bin/validatevcf
$ podman run --it --rm --entrypoint /usr/local/bin/validatevcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/validatevcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfhdr2json

```bash
$ singularity exec <container> /usr/local/bin/vcfhdr2json
$ podman run --it --rm --entrypoint /usr/local/bin/vcfhdr2json   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfhdr2json   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xcmp

```bash
$ singularity exec <container> /usr/local/bin/xcmp
$ podman run --it --rm --entrypoint /usr/local/bin/xcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfcheck

```bash
$ singularity exec <container> /usr/local/bin/vcfcheck
$ podman run --it --rm --entrypoint /usr/local/bin/vcfcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersection_matrix.py

```bash
$ singularity exec <container> /usr/local/bin/intersection_matrix.py
$ podman run --it --rm --entrypoint /usr/local/bin/intersection_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersection_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intron_exon_reads.py

```bash
$ singularity exec <container> /usr/local/bin/intron_exon_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/intron_exon_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intron_exon_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nosetests

```bash
$ singularity exec <container> /usr/local/bin/nosetests
$ podman run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbt_plotting_example.py

```bash
$ singularity exec <container> /usr/local/bin/pbt_plotting_example.py
$ podman run --it --rm --entrypoint /usr/local/bin/pbt_plotting_example.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbt_plotting_example.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### peak_pie.py

```bash
$ singularity exec <container> /usr/local/bin/peak_pie.py
$ podman run --it --rm --entrypoint /usr/local/bin/peak_pie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peak_pie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybedtools

```bash
$ singularity exec <container> /usr/local/bin/pybedtools
$ podman run --it --rm --entrypoint /usr/local/bin/pybedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### venn_gchart.py

```bash
$ singularity exec <container> /usr/local/bin/venn_gchart.py
$ podman run --it --rm --entrypoint /usr/local/bin/venn_gchart.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/venn_gchart.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### venn_mpl.py

```bash
$ singularity exec <container> /usr/local/bin/venn_mpl.py
$ podman run --it --rm --entrypoint /usr/local/bin/venn_mpl.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/venn_mpl.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate.py

```bash
$ singularity exec <container> /usr/local/bin/annotate.py
$ podman run --it --rm --entrypoint /usr/local/bin/annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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