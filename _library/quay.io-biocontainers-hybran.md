---
layout: container
name:  "quay.io/biocontainers/hybran"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hybran/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hybran/container.yaml"
updated_at: "2025-03-21 03:26:35.748121"
latest: "1.8--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/hybran"
aliases:
 - "TMalign"
 - "aria2c"
 - "create_dbs.py"
 - "download_eggnog_data.py"
 - "emapper.py"
 - "f2py3.11"
 - "hmm_mapper.py"
 - "hmm_server.py"
 - "hmm_worker.py"
 - "hybran"
 - "make_pscores.pl"
 - "poa"
 - "ratt"
 - "tbl2asn-test"
 - "2to3-3.11"
 - "clustalo"
 - "fix-sqn-date"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "faketime"
 - "real-tbl2asn"
 - "xmlget"
 - "xmltext"
 - "prokka-abricate_to_fasta_db"
 - "bl2seq"
 - "blastall"
 - "blastclust"
 - "blastpgp"
 - "copymat"
 - "fastacmd"
 - "formatdb"
 - "formatrpsdb"
 - "impala"
 - "makemat"
 - "megablast"
 - "aaindexextract"
 - "abiview"
versions:
 - "1.5.2--pyhdfd78af_1"
 - "1.6.1--pyhdfd78af_0"
 - "1.7.1--pyhdfd78af_0"
 - "1.7.1--pyhdfd78af_1"
 - "1.8--pyhdfd78af_0"
description: "singularity registry hpc automated addition for hybran"
config: {"url": "https://biocontainers.pro/tools/hybran", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hybran", "latest": {"1.8--pyhdfd78af_0": "sha256:8d36f6b6264a70d5ce05798c72710c0b0fa63a0d36168d52d6180927b28ed8fe"}, "tags": {"1.5.2--pyhdfd78af_1": "sha256:1dec647d0b88b79d3d3245818d907b82f09306dfbc2c6935623636ef0c8b5ddb", "1.6.1--pyhdfd78af_0": "sha256:089ac597b26aa627706a6dc56577b9180809bead5b65bd1d1eda89e0f3407adb", "1.7.1--pyhdfd78af_0": "sha256:c365992316c940394b6a65c5dd79260f2f5c68407b8e70996f34297a156edd7f", "1.7.1--pyhdfd78af_1": "sha256:280127bbbf400a13838eee0b438d20389d13c76871d5a2426caa481f2c059647", "1.8--pyhdfd78af_0": "sha256:8d36f6b6264a70d5ce05798c72710c0b0fa63a0d36168d52d6180927b28ed8fe"}, "docker": "quay.io/biocontainers/hybran", "aliases": {"TMalign": "/usr/local/bin/TMalign", "aria2c": "/usr/local/bin/aria2c", "create_dbs.py": "/usr/local/bin/create_dbs.py", "download_eggnog_data.py": "/usr/local/bin/download_eggnog_data.py", "emapper.py": "/usr/local/bin/emapper.py", "f2py3.11": "/usr/local/bin/f2py3.11", "hmm_mapper.py": "/usr/local/bin/hmm_mapper.py", "hmm_server.py": "/usr/local/bin/hmm_server.py", "hmm_worker.py": "/usr/local/bin/hmm_worker.py", "hybran": "/usr/local/bin/hybran", "make_pscores.pl": "/usr/local/bin/make_pscores.pl", "poa": "/usr/local/bin/poa", "ratt": "/usr/local/bin/ratt", "tbl2asn-test": "/usr/local/bin/tbl2asn-test", "2to3-3.11": "/usr/local/bin/2to3-3.11", "clustalo": "/usr/local/bin/clustalo", "fix-sqn-date": "/usr/local/bin/fix-sqn-date", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "faketime": "/usr/local/bin/faketime", "real-tbl2asn": "/usr/local/bin/real-tbl2asn", "xmlget": "/usr/local/bin/xmlget", "xmltext": "/usr/local/bin/xmltext", "prokka-abricate_to_fasta_db": "/usr/local/bin/prokka-abricate_to_fasta_db", "bl2seq": "/usr/local/bin/bl2seq", "blastall": "/usr/local/bin/blastall", "blastclust": "/usr/local/bin/blastclust", "blastpgp": "/usr/local/bin/blastpgp", "copymat": "/usr/local/bin/copymat", "fastacmd": "/usr/local/bin/fastacmd", "formatdb": "/usr/local/bin/formatdb", "formatrpsdb": "/usr/local/bin/formatrpsdb", "impala": "/usr/local/bin/impala", "makemat": "/usr/local/bin/makemat", "megablast": "/usr/local/bin/megablast", "aaindexextract": "/usr/local/bin/aaindexextract", "abiview": "/usr/local/bin/abiview"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hybran.
singularity registry hpc automated addition for hybran
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hybran
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hybran:1.8--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hybran/1.8--pyhdfd78af_0
$ module help quay.io/biocontainers/hybran/1.8--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hybran-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hybran-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hybran-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hybran-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hybran-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hybran-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### TMalign

```bash
$ singularity exec <container> /usr/local/bin/TMalign
$ podman run --it --rm --entrypoint /usr/local/bin/TMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aria2c

```bash
$ singularity exec <container> /usr/local/bin/aria2c
$ podman run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_dbs.py

```bash
$ singularity exec <container> /usr/local/bin/create_dbs.py
$ podman run --it --rm --entrypoint /usr/local/bin/create_dbs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_dbs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download_eggnog_data.py

```bash
$ singularity exec <container> /usr/local/bin/download_eggnog_data.py
$ podman run --it --rm --entrypoint /usr/local/bin/download_eggnog_data.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download_eggnog_data.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### emapper.py

```bash
$ singularity exec <container> /usr/local/bin/emapper.py
$ podman run --it --rm --entrypoint /usr/local/bin/emapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/emapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmm_mapper.py

```bash
$ singularity exec <container> /usr/local/bin/hmm_mapper.py
$ podman run --it --rm --entrypoint /usr/local/bin/hmm_mapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmm_mapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmm_server.py

```bash
$ singularity exec <container> /usr/local/bin/hmm_server.py
$ podman run --it --rm --entrypoint /usr/local/bin/hmm_server.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmm_server.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmm_worker.py

```bash
$ singularity exec <container> /usr/local/bin/hmm_worker.py
$ podman run --it --rm --entrypoint /usr/local/bin/hmm_worker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmm_worker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hybran

```bash
$ singularity exec <container> /usr/local/bin/hybran
$ podman run --it --rm --entrypoint /usr/local/bin/hybran   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hybran   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_pscores.pl

```bash
$ singularity exec <container> /usr/local/bin/make_pscores.pl
$ podman run --it --rm --entrypoint /usr/local/bin/make_pscores.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_pscores.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### poa

```bash
$ singularity exec <container> /usr/local/bin/poa
$ podman run --it --rm --entrypoint /usr/local/bin/poa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/poa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ratt

```bash
$ singularity exec <container> /usr/local/bin/ratt
$ podman run --it --rm --entrypoint /usr/local/bin/ratt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ratt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2asn-test

```bash
$ singularity exec <container> /usr/local/bin/tbl2asn-test
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2asn-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2asn-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalo

```bash
$ singularity exec <container> /usr/local/bin/clustalo
$ podman run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix-sqn-date

```bash
$ singularity exec <container> /usr/local/bin/fix-sqn-date
$ podman run --it --rm --entrypoint /usr/local/bin/fix-sqn-date   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix-sqn-date   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### faketime

```bash
$ singularity exec <container> /usr/local/bin/faketime
$ podman run --it --rm --entrypoint /usr/local/bin/faketime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faketime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### real-tbl2asn

```bash
$ singularity exec <container> /usr/local/bin/real-tbl2asn
$ podman run --it --rm --entrypoint /usr/local/bin/real-tbl2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/real-tbl2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xmlget

```bash
$ singularity exec <container> /usr/local/bin/xmlget
$ podman run --it --rm --entrypoint /usr/local/bin/xmlget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmlget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xmltext

```bash
$ singularity exec <container> /usr/local/bin/xmltext
$ podman run --it --rm --entrypoint /usr/local/bin/xmltext   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmltext   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-abricate_to_fasta_db

```bash
$ singularity exec <container> /usr/local/bin/prokka-abricate_to_fasta_db
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-abricate_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-abricate_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl2seq

```bash
$ singularity exec <container> /usr/local/bin/bl2seq
$ podman run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastall

```bash
$ singularity exec <container> /usr/local/bin/blastall
$ podman run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastclust

```bash
$ singularity exec <container> /usr/local/bin/blastclust
$ podman run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastpgp

```bash
$ singularity exec <container> /usr/local/bin/blastpgp
$ podman run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### copymat

```bash
$ singularity exec <container> /usr/local/bin/copymat
$ podman run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastacmd

```bash
$ singularity exec <container> /usr/local/bin/fastacmd
$ podman run --it --rm --entrypoint /usr/local/bin/fastacmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastacmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatdb

```bash
$ singularity exec <container> /usr/local/bin/formatdb
$ podman run --it --rm --entrypoint /usr/local/bin/formatdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatrpsdb

```bash
$ singularity exec <container> /usr/local/bin/formatrpsdb
$ podman run --it --rm --entrypoint /usr/local/bin/formatrpsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatrpsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### impala

```bash
$ singularity exec <container> /usr/local/bin/impala
$ podman run --it --rm --entrypoint /usr/local/bin/impala   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/impala   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makemat

```bash
$ singularity exec <container> /usr/local/bin/makemat
$ podman run --it --rm --entrypoint /usr/local/bin/makemat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makemat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megablast

```bash
$ singularity exec <container> /usr/local/bin/megablast
$ podman run --it --rm --entrypoint /usr/local/bin/megablast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megablast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aaindexextract

```bash
$ singularity exec <container> /usr/local/bin/aaindexextract
$ podman run --it --rm --entrypoint /usr/local/bin/aaindexextract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aaindexextract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abiview

```bash
$ singularity exec <container> /usr/local/bin/abiview
$ podman run --it --rm --entrypoint /usr/local/bin/abiview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abiview   -v ${PWD} -w ${PWD} <container> -c " $@"
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