---
layout: container
name:  "quay.io/biocontainers/isescan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/isescan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/isescan/container.yaml"
updated_at: "2024-01-11 03:47:54.209116"
latest: "1.7.2.3--h031d066_2"
container_url: "https://biocontainers.pro/tools/isescan"
aliases:
 - "FragGeneScan"
 - "constants.py"
 - "isPredict.py"
 - "is_analysis.py"
 - "isescan.py"
 - "pred.py"
 - "pyssw.py"
 - "run_FragGeneScan.pl"
 - "ssw_wrap.py"
 - "tools.py"
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
versions:
 - "1.7.2.3--hec16e2b_1"
 - "1.7.2.3--h031d066_2"
description: "shpc-registry automated BioContainers addition for isescan"
config: {"url": "https://biocontainers.pro/tools/isescan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for isescan", "latest": {"1.7.2.3--h031d066_2": "sha256:aa356d6320bd08b745eb5844885c56c94b14f3ede8270e622c94fde14896c392"}, "tags": {"1.7.2.3--hec16e2b_1": "sha256:b72103cf8c859553b3a1f829863ec86f778052ad102754ae18f3b8508db282ab", "1.7.2.3--h031d066_2": "sha256:aa356d6320bd08b745eb5844885c56c94b14f3ede8270e622c94fde14896c392"}, "docker": "quay.io/biocontainers/isescan", "aliases": {"FragGeneScan": "/usr/local/bin/FragGeneScan", "constants.py": "/usr/local/bin/constants.py", "isPredict.py": "/usr/local/bin/isPredict.py", "is_analysis.py": "/usr/local/bin/is_analysis.py", "isescan.py": "/usr/local/bin/isescan.py", "pred.py": "/usr/local/bin/pred.py", "pyssw.py": "/usr/local/bin/pyssw.py", "run_FragGeneScan.pl": "/usr/local/bin/run_FragGeneScan.pl", "ssw_wrap.py": "/usr/local/bin/ssw_wrap.py", "tools.py": "/usr/local/bin/tools.py", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments", "gene2range": "/usr/local/bin/gene2range", "tbl2prod": "/usr/local/bin/tbl2prod", "uniq-table": "/usr/local/bin/uniq-table", "align-columns": "/usr/local/bin/align-columns", "blst2tkns": "/usr/local/bin/blst2tkns", "csv2xml": "/usr/local/bin/csv2xml", "disambiguate-nucleotides": "/usr/local/bin/disambiguate-nucleotides"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/isescan.
shpc-registry automated BioContainers addition for isescan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/isescan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/isescan:1.7.2.3--h031d066_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/isescan/1.7.2.3--h031d066_2
$ module help quay.io/biocontainers/isescan/1.7.2.3--h031d066_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### isescan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### isescan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### isescan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### isescan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### isescan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### isescan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FragGeneScan

```bash
$ singularity exec <container> /usr/local/bin/FragGeneScan
$ podman run --it --rm --entrypoint /usr/local/bin/FragGeneScan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FragGeneScan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### constants.py

```bash
$ singularity exec <container> /usr/local/bin/constants.py
$ podman run --it --rm --entrypoint /usr/local/bin/constants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/constants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isPredict.py

```bash
$ singularity exec <container> /usr/local/bin/isPredict.py
$ podman run --it --rm --entrypoint /usr/local/bin/isPredict.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isPredict.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### is_analysis.py

```bash
$ singularity exec <container> /usr/local/bin/is_analysis.py
$ podman run --it --rm --entrypoint /usr/local/bin/is_analysis.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/is_analysis.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isescan.py

```bash
$ singularity exec <container> /usr/local/bin/isescan.py
$ podman run --it --rm --entrypoint /usr/local/bin/isescan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isescan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pred.py

```bash
$ singularity exec <container> /usr/local/bin/pred.py
$ podman run --it --rm --entrypoint /usr/local/bin/pred.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pred.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyssw.py

```bash
$ singularity exec <container> /usr/local/bin/pyssw.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyssw.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyssw.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_FragGeneScan.pl

```bash
$ singularity exec <container> /usr/local/bin/run_FragGeneScan.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run_FragGeneScan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_FragGeneScan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssw_wrap.py

```bash
$ singularity exec <container> /usr/local/bin/ssw_wrap.py
$ podman run --it --rm --entrypoint /usr/local/bin/ssw_wrap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssw_wrap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tools.py

```bash
$ singularity exec <container> /usr/local/bin/tools.py
$ podman run --it --rm --entrypoint /usr/local/bin/tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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