---
layout: container
name:  "quay.io/biocontainers/hpcblast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hpcblast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hpcblast/container.yaml"
updated_at: "2026-01-23 04:32:47.743087"
latest: "1.0.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/hpcblast"
aliases:
 - "hpc-blast"
 - "qcs"
 - "qs"
 - "runbatch"
 - "runjob"
 - "runsge"
 - "runshell"
 - "blastn_vdb"
 - "tblastn_vdb"
 - "uuid"
 - "uuid-config"
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
versions:
 - "1.0.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for hpcblast"
config: {"url": "https://biocontainers.pro/tools/hpcblast", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hpcblast", "latest": {"1.0.2--pyhdfd78af_0": "sha256:3f1723c9a98ffe0b97f74e91afb76a016ca871c3df9f7886076698e702426552"}, "tags": {"1.0.2--pyhdfd78af_0": "sha256:3f1723c9a98ffe0b97f74e91afb76a016ca871c3df9f7886076698e702426552"}, "docker": "quay.io/biocontainers/hpcblast", "aliases": {"hpc-blast": "/usr/local/bin/hpc-blast", "qcs": "/usr/local/bin/qcs", "qs": "/usr/local/bin/qs", "runbatch": "/usr/local/bin/runbatch", "runjob": "/usr/local/bin/runjob", "runsge": "/usr/local/bin/runsge", "runshell": "/usr/local/bin/runshell", "blastn_vdb": "/usr/local/bin/blastn_vdb", "tblastn_vdb": "/usr/local/bin/tblastn_vdb", "uuid": "/usr/local/bin/uuid", "uuid-config": "/usr/local/bin/uuid-config", "test_pcre": "/usr/local/bin/test_pcre", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments", "gene2range": "/usr/local/bin/gene2range", "tbl2prod": "/usr/local/bin/tbl2prod", "uniq-table": "/usr/local/bin/uniq-table", "align-columns": "/usr/local/bin/align-columns", "blst2tkns": "/usr/local/bin/blst2tkns", "csv2xml": "/usr/local/bin/csv2xml", "disambiguate-nucleotides": "/usr/local/bin/disambiguate-nucleotides", "download-ncbi-software": "/usr/local/bin/download-ncbi-software", "ecommon.sh": "/usr/local/bin/ecommon.sh", "find-in-gene": "/usr/local/bin/find-in-gene", "fuse-ranges": "/usr/local/bin/fuse-ranges", "hgvs2spdi": "/usr/local/bin/hgvs2spdi", "json2xml": "/usr/local/bin/json2xml", "print-columns": "/usr/local/bin/print-columns", "snp2hgvs": "/usr/local/bin/snp2hgvs", "snp2tbl": "/usr/local/bin/snp2tbl", "sort-table": "/usr/local/bin/sort-table"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hpcblast.
singularity registry hpc automated addition for hpcblast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hpcblast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hpcblast:1.0.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hpcblast/1.0.2--pyhdfd78af_0
$ module help quay.io/biocontainers/hpcblast/1.0.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hpcblast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hpcblast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hpcblast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hpcblast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hpcblast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hpcblast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hpc-blast

```bash
$ singularity exec <container> /usr/local/bin/hpc-blast
$ podman run --it --rm --entrypoint /usr/local/bin/hpc-blast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hpc-blast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qcs

```bash
$ singularity exec <container> /usr/local/bin/qcs
$ podman run --it --rm --entrypoint /usr/local/bin/qcs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qcs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qs

```bash
$ singularity exec <container> /usr/local/bin/qs
$ podman run --it --rm --entrypoint /usr/local/bin/qs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runbatch

```bash
$ singularity exec <container> /usr/local/bin/runbatch
$ podman run --it --rm --entrypoint /usr/local/bin/runbatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runbatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runjob

```bash
$ singularity exec <container> /usr/local/bin/runjob
$ podman run --it --rm --entrypoint /usr/local/bin/runjob   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runjob   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runsge

```bash
$ singularity exec <container> /usr/local/bin/runsge
$ podman run --it --rm --entrypoint /usr/local/bin/runsge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runsge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runshell

```bash
$ singularity exec <container> /usr/local/bin/runshell
$ podman run --it --rm --entrypoint /usr/local/bin/runshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runshell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastn_vdb

```bash
$ singularity exec <container> /usr/local/bin/blastn_vdb
$ podman run --it --rm --entrypoint /usr/local/bin/blastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tblastn_vdb

```bash
$ singularity exec <container> /usr/local/bin/tblastn_vdb
$ podman run --it --rm --entrypoint /usr/local/bin/tblastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tblastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uuid

```bash
$ singularity exec <container> /usr/local/bin/uuid
$ podman run --it --rm --entrypoint /usr/local/bin/uuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uuid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uuid-config

```bash
$ singularity exec <container> /usr/local/bin/uuid-config
$ podman run --it --rm --entrypoint /usr/local/bin/uuid-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uuid-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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