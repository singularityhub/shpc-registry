---
layout: container
name:  "quay.io/biocontainers/dnaapler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dnaapler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dnaapler/container.yaml"
updated_at: "2023-10-17 02:41:27.232219"
latest: "0.3.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/dnaapler"
aliases:
 - "dnaapler"
 - "pyrodigal"
 - "test_pcre"
 - "edirect.py"
 - "filter-columns"
 - "fuse-segments"
 - "gene2range"
 - "tbl2prod"
 - "uniq-table"
 - "align-columns"
 - "blst2tkns"
 - "csv2xml"
 - "disambiguate-nucleotides"
 - "download-ncbi-software"
 - "ecommon.sh"
 - "find-in-gene"
 - "fuse-ranges"
 - "hgvs2spdi"
 - "json2xml"
 - "print-columns"
 - "snp2hgvs"
 - "snp2tbl"
 - "sort-table"
 - "spdi2tbl"
 - "split-at-intron"
 - "tbl2xml"
 - "transmute.Linux"
versions:
 - "0.1.0--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_0"
 - "0.2.0--pyhdfd78af_0"
 - "0.3.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for dnaapler"
config: {"url": "https://biocontainers.pro/tools/dnaapler", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for dnaapler", "latest": {"0.3.2--pyhdfd78af_0": "sha256:367b872a1a117b1b4a5853bc514fcbdf04d4f694a55338bd7e615e113fa05e9f"}, "tags": {"0.1.0--pyhdfd78af_0": "sha256:f21c89d826bcf74ea0e9bdb574eb9d8b4dc685af03fc837abe33af53773f1e66", "0.3.0--pyhdfd78af_0": "sha256:6ae49745a944bbcd5c29b5c24ee2349937bba1e6e95978d4403dc014966884cc", "0.2.0--pyhdfd78af_0": "sha256:afbf56ef8a9387897ea08722b29b1512dc7bd9b9d95e773c78745b6d3d9e4516", "0.3.2--pyhdfd78af_0": "sha256:367b872a1a117b1b4a5853bc514fcbdf04d4f694a55338bd7e615e113fa05e9f"}, "docker": "quay.io/biocontainers/dnaapler", "aliases": {"dnaapler": "/usr/local/bin/dnaapler", "pyrodigal": "/usr/local/bin/pyrodigal", "test_pcre": "/usr/local/bin/test_pcre", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments", "gene2range": "/usr/local/bin/gene2range", "tbl2prod": "/usr/local/bin/tbl2prod", "uniq-table": "/usr/local/bin/uniq-table", "align-columns": "/usr/local/bin/align-columns", "blst2tkns": "/usr/local/bin/blst2tkns", "csv2xml": "/usr/local/bin/csv2xml", "disambiguate-nucleotides": "/usr/local/bin/disambiguate-nucleotides", "download-ncbi-software": "/usr/local/bin/download-ncbi-software", "ecommon.sh": "/usr/local/bin/ecommon.sh", "find-in-gene": "/usr/local/bin/find-in-gene", "fuse-ranges": "/usr/local/bin/fuse-ranges", "hgvs2spdi": "/usr/local/bin/hgvs2spdi", "json2xml": "/usr/local/bin/json2xml", "print-columns": "/usr/local/bin/print-columns", "snp2hgvs": "/usr/local/bin/snp2hgvs", "snp2tbl": "/usr/local/bin/snp2tbl", "sort-table": "/usr/local/bin/sort-table", "spdi2tbl": "/usr/local/bin/spdi2tbl", "split-at-intron": "/usr/local/bin/split-at-intron", "tbl2xml": "/usr/local/bin/tbl2xml", "transmute.Linux": "/usr/local/bin/transmute.Linux"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dnaapler.
singularity registry hpc automated addition for dnaapler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dnaapler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dnaapler:0.3.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dnaapler/0.3.2--pyhdfd78af_0
$ module help quay.io/biocontainers/dnaapler/0.3.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dnaapler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dnaapler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dnaapler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dnaapler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dnaapler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dnaapler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dnaapler

```bash
$ singularity exec <container> /usr/local/bin/dnaapler
$ podman run --it --rm --entrypoint /usr/local/bin/dnaapler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnaapler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrodigal

```bash
$ singularity exec <container> /usr/local/bin/pyrodigal
$ podman run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_pcre

```bash
$ singularity exec <container> /usr/local/bin/test_pcre
$ podman run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edirect.py

```bash
$ singularity exec <container> /usr/local/bin/edirect.py
$ podman run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-columns

```bash
$ singularity exec <container> /usr/local/bin/filter-columns
$ podman run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuse-segments

```bash
$ singularity exec <container> /usr/local/bin/fuse-segments
$ podman run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene2range

```bash
$ singularity exec <container> /usr/local/bin/gene2range
$ podman run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2prod

```bash
$ singularity exec <container> /usr/local/bin/tbl2prod
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniq-table

```bash
$ singularity exec <container> /usr/local/bin/uniq-table
$ podman run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align-columns

```bash
$ singularity exec <container> /usr/local/bin/align-columns
$ podman run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blst2tkns

```bash
$ singularity exec <container> /usr/local/bin/blst2tkns
$ podman run --it --rm --entrypoint /usr/local/bin/blst2tkns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blst2tkns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv2xml

```bash
$ singularity exec <container> /usr/local/bin/csv2xml
$ podman run --it --rm --entrypoint /usr/local/bin/csv2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### disambiguate-nucleotides

```bash
$ singularity exec <container> /usr/local/bin/disambiguate-nucleotides
$ podman run --it --rm --entrypoint /usr/local/bin/disambiguate-nucleotides   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/disambiguate-nucleotides   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-ncbi-software

```bash
$ singularity exec <container> /usr/local/bin/download-ncbi-software
$ podman run --it --rm --entrypoint /usr/local/bin/download-ncbi-software   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-ncbi-software   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecommon.sh

```bash
$ singularity exec <container> /usr/local/bin/ecommon.sh
$ podman run --it --rm --entrypoint /usr/local/bin/ecommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find-in-gene

```bash
$ singularity exec <container> /usr/local/bin/find-in-gene
$ podman run --it --rm --entrypoint /usr/local/bin/find-in-gene   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find-in-gene   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuse-ranges

```bash
$ singularity exec <container> /usr/local/bin/fuse-ranges
$ podman run --it --rm --entrypoint /usr/local/bin/fuse-ranges   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuse-ranges   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hgvs2spdi

```bash
$ singularity exec <container> /usr/local/bin/hgvs2spdi
$ podman run --it --rm --entrypoint /usr/local/bin/hgvs2spdi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hgvs2spdi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### json2xml

```bash
$ singularity exec <container> /usr/local/bin/json2xml
$ podman run --it --rm --entrypoint /usr/local/bin/json2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/json2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### print-columns

```bash
$ singularity exec <container> /usr/local/bin/print-columns
$ podman run --it --rm --entrypoint /usr/local/bin/print-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/print-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snp2hgvs

```bash
$ singularity exec <container> /usr/local/bin/snp2hgvs
$ podman run --it --rm --entrypoint /usr/local/bin/snp2hgvs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snp2hgvs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snp2tbl

```bash
$ singularity exec <container> /usr/local/bin/snp2tbl
$ podman run --it --rm --entrypoint /usr/local/bin/snp2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snp2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sort-table

```bash
$ singularity exec <container> /usr/local/bin/sort-table
$ podman run --it --rm --entrypoint /usr/local/bin/sort-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sort-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spdi2tbl

```bash
$ singularity exec <container> /usr/local/bin/spdi2tbl
$ podman run --it --rm --entrypoint /usr/local/bin/spdi2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spdi2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split-at-intron

```bash
$ singularity exec <container> /usr/local/bin/split-at-intron
$ podman run --it --rm --entrypoint /usr/local/bin/split-at-intron   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split-at-intron   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2xml

```bash
$ singularity exec <container> /usr/local/bin/tbl2xml
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transmute.Linux

```bash
$ singularity exec <container> /usr/local/bin/transmute.Linux
$ podman run --it --rm --entrypoint /usr/local/bin/transmute.Linux   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transmute.Linux   -v ${PWD} -w ${PWD} <container> -c " $@"
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