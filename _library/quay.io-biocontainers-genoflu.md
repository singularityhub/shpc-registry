---
layout: container
name:  "quay.io/biocontainers/genoflu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genoflu/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genoflu/container.yaml"
updated_at: "2025-02-21 03:25:57.639627"
latest: "1.06--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/genoflu"
aliases:
 - "genoflu.py"
 - "test_pcre"
 - "f2py3.11"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
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
versions:
 - "1.0--hdfd78af_0"
 - "1.01--hdfd78af_0"
 - "1.02--hdfd78af_0"
 - "1.03--hdfd78af_0"
 - "1.05--hdfd78af_0"
 - "1.04--hdfd78af_0"
 - "1.06--hdfd78af_0"
description: "singularity registry hpc automated addition for genoflu"
config: {"url": "https://biocontainers.pro/tools/genoflu", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for genoflu", "latest": {"1.06--hdfd78af_0": "sha256:50ba467f890fbc924d67e6a66302bffaf5123d21e3de14ea54ddf3b700442a59"}, "tags": {"1.0--hdfd78af_0": "sha256:827ff2d56128685ce061c09244a6788ccaeee692e32f4d7dfcca193d6397e59a", "1.01--hdfd78af_0": "sha256:700abcb4ae89f74e337ccf7d82ce291e9aa3cb712239e34659caf6f462dc1883", "1.02--hdfd78af_0": "sha256:2e9cc005c3c6400e9f09bfb4a3417a9d00d0c8f1b6b4ab3bb6e538987bbd8bdd", "1.03--hdfd78af_0": "sha256:ca1c17846d8d6f5b32e5e99128220efc38d4992c86cdcc3403075a1e9ae44c6b", "1.05--hdfd78af_0": "sha256:670deda5539cb3d1abc33e66652fad360b846d5022bc520e1093db157e6e00da", "1.04--hdfd78af_0": "sha256:335d71f7a6a0266df69768eae18f0a340a682dd16db5d7ea992ff23ae30b3a88", "1.06--hdfd78af_0": "sha256:50ba467f890fbc924d67e6a66302bffaf5123d21e3de14ea54ddf3b700442a59"}, "docker": "quay.io/biocontainers/genoflu", "aliases": {"genoflu.py": "/usr/local/bin/genoflu.py", "test_pcre": "/usr/local/bin/test_pcre", "f2py3.11": "/usr/local/bin/f2py3.11", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments", "gene2range": "/usr/local/bin/gene2range", "tbl2prod": "/usr/local/bin/tbl2prod", "uniq-table": "/usr/local/bin/uniq-table", "align-columns": "/usr/local/bin/align-columns", "blst2tkns": "/usr/local/bin/blst2tkns", "csv2xml": "/usr/local/bin/csv2xml", "disambiguate-nucleotides": "/usr/local/bin/disambiguate-nucleotides", "download-ncbi-software": "/usr/local/bin/download-ncbi-software", "ecommon.sh": "/usr/local/bin/ecommon.sh", "find-in-gene": "/usr/local/bin/find-in-gene", "fuse-ranges": "/usr/local/bin/fuse-ranges", "hgvs2spdi": "/usr/local/bin/hgvs2spdi", "json2xml": "/usr/local/bin/json2xml", "print-columns": "/usr/local/bin/print-columns", "snp2hgvs": "/usr/local/bin/snp2hgvs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genoflu.
singularity registry hpc automated addition for genoflu
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genoflu
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genoflu:1.06--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genoflu/1.06--hdfd78af_0
$ module help quay.io/biocontainers/genoflu/1.06--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genoflu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genoflu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genoflu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genoflu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genoflu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genoflu-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### genoflu.py

```bash
$ singularity exec <container> /usr/local/bin/genoflu.py
$ podman run --it --rm --entrypoint /usr/local/bin/genoflu.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genoflu.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_pcre

```bash
$ singularity exec <container> /usr/local/bin/test_pcre
$ podman run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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