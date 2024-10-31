---
layout: container
name:  "quay.io/biocontainers/tf-comb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tf-comb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tf-comb/container.yaml"
updated_at: "2024-10-31 00:34:30.845240"
latest: "1.1--py39hec7c8de_0"
container_url: "https://biocontainers.pro/tools/tf-comb"
aliases:
 - "TOBIAS"
 - "cluster_sites_by_overlap.py"
 - "community"
 - "compare_gos.py"
 - "fetch_associations.py"
 - "filter_important_factors.py"
 - "find_enrichment.py"
 - "get_gprof"
 - "go_plot.py"
 - "map_to_slim.py"
 - "moods-dna.py"
 - "ncbi_gene_results_to_python.py"
 - "plot_go_term.py"
 - "prt_terms.py"
 - "qnorm"
 - "svist4get"
 - "svist4get_copier"
 - "uropa"
 - "uropa2gtf.R"
 - "uropa_summary.R"
 - "wr_hier.py"
 - "wr_sections.py"
 - "ccache-swig"
 - "swig"
 - "mpg123"
 - "mpg123-id3dump"
 - "mpg123-strip"
 - "out123"
 - "xgboost"
 - "dumpsexp"
 - "gpg-error"
 - "gpgrt-config"
 - "hmac256"
 - "libgcrypt-config"
 - "mpicalc"
 - "yat2m"
 - "lame"
 - "markdown-it"
 - "sip-build"
 - "sip-distinfo"
 - "sip-install"
 - "sip-module"
 - "sip-sdist"
 - "sip-wheel"
 - "attr"
 - "balsam"
 - "getfattr"
versions:
 - "1.1--py39hec7c8de_0"
 - "1.1--py38h24c8ff8_0"
description: "singularity registry hpc automated addition for tf-comb"
config: {"url": "https://biocontainers.pro/tools/tf-comb", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for tf-comb", "latest": {"1.1--py39hec7c8de_0": "sha256:a119197f0e84cf48a70a5131678390578d0dbc86a7c31ecda05d1fd9051af8d3"}, "tags": {"1.1--py39hec7c8de_0": "sha256:a119197f0e84cf48a70a5131678390578d0dbc86a7c31ecda05d1fd9051af8d3", "1.1--py38h24c8ff8_0": "sha256:68199aefd40123533c76d3d3106869af0b00bcfa31b66e875f44ff4da16f566b"}, "docker": "quay.io/biocontainers/tf-comb", "aliases": {"TOBIAS": "/usr/local/bin/TOBIAS", "cluster_sites_by_overlap.py": "/usr/local/bin/cluster_sites_by_overlap.py", "community": "/usr/local/bin/community", "compare_gos.py": "/usr/local/bin/compare_gos.py", "fetch_associations.py": "/usr/local/bin/fetch_associations.py", "filter_important_factors.py": "/usr/local/bin/filter_important_factors.py", "find_enrichment.py": "/usr/local/bin/find_enrichment.py", "get_gprof": "/usr/local/bin/get_gprof", "go_plot.py": "/usr/local/bin/go_plot.py", "map_to_slim.py": "/usr/local/bin/map_to_slim.py", "moods-dna.py": "/usr/local/bin/moods-dna.py", "ncbi_gene_results_to_python.py": "/usr/local/bin/ncbi_gene_results_to_python.py", "plot_go_term.py": "/usr/local/bin/plot_go_term.py", "prt_terms.py": "/usr/local/bin/prt_terms.py", "qnorm": "/usr/local/bin/qnorm", "svist4get": "/usr/local/bin/svist4get", "svist4get_copier": "/usr/local/bin/svist4get_copier", "uropa": "/usr/local/bin/uropa", "uropa2gtf.R": "/usr/local/bin/uropa2gtf.R", "uropa_summary.R": "/usr/local/bin/uropa_summary.R", "wr_hier.py": "/usr/local/bin/wr_hier.py", "wr_sections.py": "/usr/local/bin/wr_sections.py", "ccache-swig": "/usr/local/bin/ccache-swig", "swig": "/usr/local/bin/swig", "mpg123": "/usr/local/bin/mpg123", "mpg123-id3dump": "/usr/local/bin/mpg123-id3dump", "mpg123-strip": "/usr/local/bin/mpg123-strip", "out123": "/usr/local/bin/out123", "xgboost": "/usr/local/bin/xgboost", "dumpsexp": "/usr/local/bin/dumpsexp", "gpg-error": "/usr/local/bin/gpg-error", "gpgrt-config": "/usr/local/bin/gpgrt-config", "hmac256": "/usr/local/bin/hmac256", "libgcrypt-config": "/usr/local/bin/libgcrypt-config", "mpicalc": "/usr/local/bin/mpicalc", "yat2m": "/usr/local/bin/yat2m", "lame": "/usr/local/bin/lame", "markdown-it": "/usr/local/bin/markdown-it", "sip-build": "/usr/local/bin/sip-build", "sip-distinfo": "/usr/local/bin/sip-distinfo", "sip-install": "/usr/local/bin/sip-install", "sip-module": "/usr/local/bin/sip-module", "sip-sdist": "/usr/local/bin/sip-sdist", "sip-wheel": "/usr/local/bin/sip-wheel", "attr": "/usr/local/bin/attr", "balsam": "/usr/local/bin/balsam", "getfattr": "/usr/local/bin/getfattr"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tf-comb.
singularity registry hpc automated addition for tf-comb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tf-comb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tf-comb:1.1--py39hec7c8de_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tf-comb/1.1--py39hec7c8de_0
$ module help quay.io/biocontainers/tf-comb/1.1--py39hec7c8de_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tf-comb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tf-comb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tf-comb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tf-comb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tf-comb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tf-comb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### TOBIAS

```bash
$ singularity exec <container> /usr/local/bin/TOBIAS
$ podman run --it --rm --entrypoint /usr/local/bin/TOBIAS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TOBIAS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cluster_sites_by_overlap.py

```bash
$ singularity exec <container> /usr/local/bin/cluster_sites_by_overlap.py
$ podman run --it --rm --entrypoint /usr/local/bin/cluster_sites_by_overlap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cluster_sites_by_overlap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### community

```bash
$ singularity exec <container> /usr/local/bin/community
$ podman run --it --rm --entrypoint /usr/local/bin/community   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/community   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare_gos.py

```bash
$ singularity exec <container> /usr/local/bin/compare_gos.py
$ podman run --it --rm --entrypoint /usr/local/bin/compare_gos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare_gos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch_associations.py

```bash
$ singularity exec <container> /usr/local/bin/fetch_associations.py
$ podman run --it --rm --entrypoint /usr/local/bin/fetch_associations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch_associations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_important_factors.py

```bash
$ singularity exec <container> /usr/local/bin/filter_important_factors.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_important_factors.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_important_factors.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find_enrichment.py

```bash
$ singularity exec <container> /usr/local/bin/find_enrichment.py
$ podman run --it --rm --entrypoint /usr/local/bin/find_enrichment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_enrichment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_gprof

```bash
$ singularity exec <container> /usr/local/bin/get_gprof
$ podman run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go_plot.py

```bash
$ singularity exec <container> /usr/local/bin/go_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/go_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map_to_slim.py

```bash
$ singularity exec <container> /usr/local/bin/map_to_slim.py
$ podman run --it --rm --entrypoint /usr/local/bin/map_to_slim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map_to_slim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### moods-dna.py

```bash
$ singularity exec <container> /usr/local/bin/moods-dna.py
$ podman run --it --rm --entrypoint /usr/local/bin/moods-dna.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/moods-dna.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncbi_gene_results_to_python.py

```bash
$ singularity exec <container> /usr/local/bin/ncbi_gene_results_to_python.py
$ podman run --it --rm --entrypoint /usr/local/bin/ncbi_gene_results_to_python.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncbi_gene_results_to_python.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_go_term.py

```bash
$ singularity exec <container> /usr/local/bin/plot_go_term.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot_go_term.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_go_term.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prt_terms.py

```bash
$ singularity exec <container> /usr/local/bin/prt_terms.py
$ podman run --it --rm --entrypoint /usr/local/bin/prt_terms.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prt_terms.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qnorm

```bash
$ singularity exec <container> /usr/local/bin/qnorm
$ podman run --it --rm --entrypoint /usr/local/bin/qnorm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qnorm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svist4get

```bash
$ singularity exec <container> /usr/local/bin/svist4get
$ podman run --it --rm --entrypoint /usr/local/bin/svist4get   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svist4get   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svist4get_copier

```bash
$ singularity exec <container> /usr/local/bin/svist4get_copier
$ podman run --it --rm --entrypoint /usr/local/bin/svist4get_copier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svist4get_copier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uropa

```bash
$ singularity exec <container> /usr/local/bin/uropa
$ podman run --it --rm --entrypoint /usr/local/bin/uropa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uropa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uropa2gtf.R

```bash
$ singularity exec <container> /usr/local/bin/uropa2gtf.R
$ podman run --it --rm --entrypoint /usr/local/bin/uropa2gtf.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uropa2gtf.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uropa_summary.R

```bash
$ singularity exec <container> /usr/local/bin/uropa_summary.R
$ podman run --it --rm --entrypoint /usr/local/bin/uropa_summary.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uropa_summary.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wr_hier.py

```bash
$ singularity exec <container> /usr/local/bin/wr_hier.py
$ podman run --it --rm --entrypoint /usr/local/bin/wr_hier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wr_hier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wr_sections.py

```bash
$ singularity exec <container> /usr/local/bin/wr_sections.py
$ podman run --it --rm --entrypoint /usr/local/bin/wr_sections.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wr_sections.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccache-swig

```bash
$ singularity exec <container> /usr/local/bin/ccache-swig
$ podman run --it --rm --entrypoint /usr/local/bin/ccache-swig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccache-swig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### swig

```bash
$ singularity exec <container> /usr/local/bin/swig
$ podman run --it --rm --entrypoint /usr/local/bin/swig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/swig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpg123

```bash
$ singularity exec <container> /usr/local/bin/mpg123
$ podman run --it --rm --entrypoint /usr/local/bin/mpg123   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpg123   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpg123-id3dump

```bash
$ singularity exec <container> /usr/local/bin/mpg123-id3dump
$ podman run --it --rm --entrypoint /usr/local/bin/mpg123-id3dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpg123-id3dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpg123-strip

```bash
$ singularity exec <container> /usr/local/bin/mpg123-strip
$ podman run --it --rm --entrypoint /usr/local/bin/mpg123-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpg123-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### out123

```bash
$ singularity exec <container> /usr/local/bin/out123
$ podman run --it --rm --entrypoint /usr/local/bin/out123   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/out123   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xgboost

```bash
$ singularity exec <container> /usr/local/bin/xgboost
$ podman run --it --rm --entrypoint /usr/local/bin/xgboost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xgboost   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dumpsexp

```bash
$ singularity exec <container> /usr/local/bin/dumpsexp
$ podman run --it --rm --entrypoint /usr/local/bin/dumpsexp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dumpsexp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpg-error

```bash
$ singularity exec <container> /usr/local/bin/gpg-error
$ podman run --it --rm --entrypoint /usr/local/bin/gpg-error   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpg-error   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpgrt-config

```bash
$ singularity exec <container> /usr/local/bin/gpgrt-config
$ podman run --it --rm --entrypoint /usr/local/bin/gpgrt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpgrt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmac256

```bash
$ singularity exec <container> /usr/local/bin/hmac256
$ podman run --it --rm --entrypoint /usr/local/bin/hmac256   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmac256   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libgcrypt-config

```bash
$ singularity exec <container> /usr/local/bin/libgcrypt-config
$ podman run --it --rm --entrypoint /usr/local/bin/libgcrypt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libgcrypt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpicalc

```bash
$ singularity exec <container> /usr/local/bin/mpicalc
$ podman run --it --rm --entrypoint /usr/local/bin/mpicalc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpicalc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yat2m

```bash
$ singularity exec <container> /usr/local/bin/yat2m
$ podman run --it --rm --entrypoint /usr/local/bin/yat2m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yat2m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lame

```bash
$ singularity exec <container> /usr/local/bin/lame
$ podman run --it --rm --entrypoint /usr/local/bin/lame   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lame   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-build

```bash
$ singularity exec <container> /usr/local/bin/sip-build
$ podman run --it --rm --entrypoint /usr/local/bin/sip-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-distinfo

```bash
$ singularity exec <container> /usr/local/bin/sip-distinfo
$ podman run --it --rm --entrypoint /usr/local/bin/sip-distinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-distinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-install

```bash
$ singularity exec <container> /usr/local/bin/sip-install
$ podman run --it --rm --entrypoint /usr/local/bin/sip-install   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-install   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-module

```bash
$ singularity exec <container> /usr/local/bin/sip-module
$ podman run --it --rm --entrypoint /usr/local/bin/sip-module   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-module   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-sdist

```bash
$ singularity exec <container> /usr/local/bin/sip-sdist
$ podman run --it --rm --entrypoint /usr/local/bin/sip-sdist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-sdist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-wheel

```bash
$ singularity exec <container> /usr/local/bin/sip-wheel
$ podman run --it --rm --entrypoint /usr/local/bin/sip-wheel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-wheel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### attr

```bash
$ singularity exec <container> /usr/local/bin/attr
$ podman run --it --rm --entrypoint /usr/local/bin/attr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/attr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### balsam

```bash
$ singularity exec <container> /usr/local/bin/balsam
$ podman run --it --rm --entrypoint /usr/local/bin/balsam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/balsam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getfattr

```bash
$ singularity exec <container> /usr/local/bin/getfattr
$ podman run --it --rm --entrypoint /usr/local/bin/getfattr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getfattr   -v ${PWD} -w ${PWD} <container> -c " $@"
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