---
layout: container
name:  "quay.io/biocontainers/anansnake"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/anansnake/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/anansnake/container.yaml"
updated_at: "2023-12-04 03:31:49.433762"
latest: "0.1.0--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/anansnake"
aliases:
 - "anansnake"
 - "bedToGenePred"
 - "bsdcat"
 - "bsdcpio"
 - "bsdtar"
 - "conda2solv"
 - "deseq2science"
 - "dumpsolv"
 - "genePredToBed"
 - "genePredToGtf"
 - "genomepy"
 - "gff3ToGenePred"
 - "gtfToGenePred"
 - "installcheck"
 - "mamba"
 - "mamba-package"
 - "matplotlib"
 - "mergesolv"
 - "pysradb"
 - "repo2solv"
 - "seq2science"
 - "testsolv"
 - "nosetests-3.9"
 - "conda-env"
 - "cph"
 - "plac_runner.py"
 - "yte"
 - "docutils"
 - "nosetests"
 - "pulptest"
 - "cbc"
 - "clp"
 - "vcf_sample_filter.py"
 - "vcf_filter.py"
 - "vcf_melt"
 - "snakemake"
 - "snakemake-bash-completion"
 - "tabulate"
 - "jupyter-trust"
 - "faidx"
 - "jupyter"
 - "jupyter-migrate"
 - "jupyter-troubleshoot"
 - "my_print_defaults"
 - "mysql_config"
 - "perror"
 - "rst2html4.py"
versions:
 - "0.0.1--pyhdfd78af_0"
 - "0.1.0--pyh7cba7a3_0"
description: "singularity registry hpc automated addition for anansnake"
config: {"url": "https://biocontainers.pro/tools/anansnake", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for anansnake", "latest": {"0.1.0--pyh7cba7a3_0": "sha256:52d2d433914b95ca54829d55e118c59225cc41e1b4eafdc1017db16e8aac86a1"}, "tags": {"0.0.1--pyhdfd78af_0": "sha256:25ba907a0f5696774c2cb50402d533596af215c02c9aaa65c64b0c19321a5e96", "0.1.0--pyh7cba7a3_0": "sha256:52d2d433914b95ca54829d55e118c59225cc41e1b4eafdc1017db16e8aac86a1"}, "docker": "quay.io/biocontainers/anansnake", "aliases": {"anansnake": "/usr/local/bin/anansnake", "bedToGenePred": "/usr/local/bin/bedToGenePred", "bsdcat": "/usr/local/bin/bsdcat", "bsdcpio": "/usr/local/bin/bsdcpio", "bsdtar": "/usr/local/bin/bsdtar", "conda2solv": "/usr/local/bin/conda2solv", "deseq2science": "/usr/local/bin/deseq2science", "dumpsolv": "/usr/local/bin/dumpsolv", "genePredToBed": "/usr/local/bin/genePredToBed", "genePredToGtf": "/usr/local/bin/genePredToGtf", "genomepy": "/usr/local/bin/genomepy", "gff3ToGenePred": "/usr/local/bin/gff3ToGenePred", "gtfToGenePred": "/usr/local/bin/gtfToGenePred", "installcheck": "/usr/local/bin/installcheck", "mamba": "/usr/local/bin/mamba", "mamba-package": "/usr/local/bin/mamba-package", "matplotlib": "/usr/local/bin/matplotlib", "mergesolv": "/usr/local/bin/mergesolv", "pysradb": "/usr/local/bin/pysradb", "repo2solv": "/usr/local/bin/repo2solv", "seq2science": "/usr/local/bin/seq2science", "testsolv": "/usr/local/bin/testsolv", "nosetests-3.9": "/usr/local/bin/nosetests-3.9", "conda-env": "/usr/local/bin/conda-env", "cph": "/usr/local/bin/cph", "plac_runner.py": "/usr/local/bin/plac_runner.py", "yte": "/usr/local/bin/yte", "docutils": "/usr/local/bin/docutils", "nosetests": "/usr/local/bin/nosetests", "pulptest": "/usr/local/bin/pulptest", "cbc": "/usr/local/bin/cbc", "clp": "/usr/local/bin/clp", "vcf_sample_filter.py": "/usr/local/bin/vcf_sample_filter.py", "vcf_filter.py": "/usr/local/bin/vcf_filter.py", "vcf_melt": "/usr/local/bin/vcf_melt", "snakemake": "/usr/local/bin/snakemake", "snakemake-bash-completion": "/usr/local/bin/snakemake-bash-completion", "tabulate": "/usr/local/bin/tabulate", "jupyter-trust": "/usr/local/bin/jupyter-trust", "faidx": "/usr/local/bin/faidx", "jupyter": "/usr/local/bin/jupyter", "jupyter-migrate": "/usr/local/bin/jupyter-migrate", "jupyter-troubleshoot": "/usr/local/bin/jupyter-troubleshoot", "my_print_defaults": "/usr/local/bin/my_print_defaults", "mysql_config": "/usr/local/bin/mysql_config", "perror": "/usr/local/bin/perror", "rst2html4.py": "/usr/local/bin/rst2html4.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/anansnake.
singularity registry hpc automated addition for anansnake
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/anansnake
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/anansnake:0.1.0--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/anansnake/0.1.0--pyh7cba7a3_0
$ module help quay.io/biocontainers/anansnake/0.1.0--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### anansnake-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### anansnake-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### anansnake-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### anansnake-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### anansnake-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### anansnake-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### anansnake

```bash
$ singularity exec <container> /usr/local/bin/anansnake
$ podman run --it --rm --entrypoint /usr/local/bin/anansnake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/anansnake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToGenePred

```bash
$ singularity exec <container> /usr/local/bin/bedToGenePred
$ podman run --it --rm --entrypoint /usr/local/bin/bedToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdcat

```bash
$ singularity exec <container> /usr/local/bin/bsdcat
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdcpio

```bash
$ singularity exec <container> /usr/local/bin/bsdcpio
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdtar

```bash
$ singularity exec <container> /usr/local/bin/bsdtar
$ podman run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda2solv

```bash
$ singularity exec <container> /usr/local/bin/conda2solv
$ podman run --it --rm --entrypoint /usr/local/bin/conda2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deseq2science

```bash
$ singularity exec <container> /usr/local/bin/deseq2science
$ podman run --it --rm --entrypoint /usr/local/bin/deseq2science   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deseq2science   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dumpsolv

```bash
$ singularity exec <container> /usr/local/bin/dumpsolv
$ podman run --it --rm --entrypoint /usr/local/bin/dumpsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dumpsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genePredToBed

```bash
$ singularity exec <container> /usr/local/bin/genePredToBed
$ podman run --it --rm --entrypoint /usr/local/bin/genePredToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genePredToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genePredToGtf

```bash
$ singularity exec <container> /usr/local/bin/genePredToGtf
$ podman run --it --rm --entrypoint /usr/local/bin/genePredToGtf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genePredToGtf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomepy

```bash
$ singularity exec <container> /usr/local/bin/genomepy
$ podman run --it --rm --entrypoint /usr/local/bin/genomepy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomepy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3ToGenePred

```bash
$ singularity exec <container> /usr/local/bin/gff3ToGenePred
$ podman run --it --rm --entrypoint /usr/local/bin/gff3ToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3ToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtfToGenePred

```bash
$ singularity exec <container> /usr/local/bin/gtfToGenePred
$ podman run --it --rm --entrypoint /usr/local/bin/gtfToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtfToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### installcheck

```bash
$ singularity exec <container> /usr/local/bin/installcheck
$ podman run --it --rm --entrypoint /usr/local/bin/installcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/installcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mamba

```bash
$ singularity exec <container> /usr/local/bin/mamba
$ podman run --it --rm --entrypoint /usr/local/bin/mamba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mamba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mamba-package

```bash
$ singularity exec <container> /usr/local/bin/mamba-package
$ podman run --it --rm --entrypoint /usr/local/bin/mamba-package   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mamba-package   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### matplotlib

```bash
$ singularity exec <container> /usr/local/bin/matplotlib
$ podman run --it --rm --entrypoint /usr/local/bin/matplotlib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/matplotlib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergesolv

```bash
$ singularity exec <container> /usr/local/bin/mergesolv
$ podman run --it --rm --entrypoint /usr/local/bin/mergesolv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergesolv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pysradb

```bash
$ singularity exec <container> /usr/local/bin/pysradb
$ podman run --it --rm --entrypoint /usr/local/bin/pysradb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pysradb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repo2solv

```bash
$ singularity exec <container> /usr/local/bin/repo2solv
$ podman run --it --rm --entrypoint /usr/local/bin/repo2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repo2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq2science

```bash
$ singularity exec <container> /usr/local/bin/seq2science
$ podman run --it --rm --entrypoint /usr/local/bin/seq2science   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq2science   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testsolv

```bash
$ singularity exec <container> /usr/local/bin/testsolv
$ podman run --it --rm --entrypoint /usr/local/bin/testsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nosetests-3.9

```bash
$ singularity exec <container> /usr/local/bin/nosetests-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/nosetests-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nosetests-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-env

```bash
$ singularity exec <container> /usr/local/bin/conda-env
$ podman run --it --rm --entrypoint /usr/local/bin/conda-env   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-env   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cph

```bash
$ singularity exec <container> /usr/local/bin/cph
$ podman run --it --rm --entrypoint /usr/local/bin/cph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plac_runner.py

```bash
$ singularity exec <container> /usr/local/bin/plac_runner.py
$ podman run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yte

```bash
$ singularity exec <container> /usr/local/bin/yte
$ podman run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nosetests

```bash
$ singularity exec <container> /usr/local/bin/nosetests
$ podman run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pulptest

```bash
$ singularity exec <container> /usr/local/bin/pulptest
$ podman run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### snakemake

```bash
$ singularity exec <container> /usr/local/bin/snakemake
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake-bash-completion

```bash
$ singularity exec <container> /usr/local/bin/snakemake-bash-completion
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabulate

```bash
$ singularity exec <container> /usr/local/bin/tabulate
$ podman run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-trust

```bash
$ singularity exec <container> /usr/local/bin/jupyter-trust
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faidx

```bash
$ singularity exec <container> /usr/local/bin/faidx
$ podman run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter

```bash
$ singularity exec <container> /usr/local/bin/jupyter
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-migrate

```bash
$ singularity exec <container> /usr/local/bin/jupyter-migrate
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-troubleshoot

```bash
$ singularity exec <container> /usr/local/bin/jupyter-troubleshoot
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-troubleshoot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-troubleshoot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### my_print_defaults

```bash
$ singularity exec <container> /usr/local/bin/my_print_defaults
$ podman run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_config

```bash
$ singularity exec <container> /usr/local/bin/mysql_config
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perror

```bash
$ singularity exec <container> /usr/local/bin/perror
$ podman run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html4.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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