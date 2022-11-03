---
layout: container
name:  "quay.io/biocontainers/batch_brb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/batch_brb/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/batch_brb/container.yaml"
updated_at: "2022-11-03 01:18:42.702861"
latest: "1.0.1--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/batch_brb"
aliases:
 - "accession_retrieve"
 - "adb01_check_db.py"
 - "adb02_add_alias_to_db.py"
 - "aliasdb_pipeline"
 - "alncut"
 - "alnpi"
 - "ar01_accret.py"
 - "bash"
 - "bashbug"
 - "batch_brb_functions.py"
 - "batch_brb_setup"
 - "batch_makeblastdb"
 - "del01_delete_db_entries.py"
 - "delete_db"
 - "fascodon"
 - "fascomp"
 - "fasconvert"
 - "fascut"
 - "fasfilter"
 - "fasgrep"
 - "fashead"
 - "faslen"
 - "faspaste"
 - "fasrc"
 - "fassort"
 - "fassub"
 - "fastail"
 - "fastax"
 - "fastaxsort"
 - "fastr"
 - "fasttree_pipeline"
 - "fasuniq"
 - "faswc"
 - "fasxl"
 - "ft01_extract_accessions.py"
 - "gbfalncut"
 - "gbfcut"
 - "mdb01_makeblastdb.sh"
 - "mdb02_convert_headers.py"
 - "mdb03_add_to_db.py"
 - "merge_results"
 - "or01_filter_hits.py"
 - "or02_find_orthologs.py"
 - "orthology_pipeline"
 - "show"
 - "seqkit"
 - "FastTree-2.1.10.c"
 - "FastTreeMP"
 - "muscle"
 - "FastTree"
 - "fasttree"
 - "CA.pm"
 - "cacert.pem"
 - "index-themes"
 - "fetch-extras"
versions:
 - "1.0.1--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for batch_brb"
config: {"url": "https://biocontainers.pro/tools/batch_brb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for batch_brb", "latest": {"1.0.1--hdfd78af_1": "sha256:20d4acd2727188ad223929fd69f168b0169c0bc6c9d831aa225bc786b43fae33"}, "tags": {"1.0.1--hdfd78af_1": "sha256:20d4acd2727188ad223929fd69f168b0169c0bc6c9d831aa225bc786b43fae33"}, "docker": "quay.io/biocontainers/batch_brb", "aliases": {"accession_retrieve": "/usr/local/bin/accession_retrieve", "adb01_check_db.py": "/usr/local/bin/adb01_check_db.py", "adb02_add_alias_to_db.py": "/usr/local/bin/adb02_add_alias_to_db.py", "aliasdb_pipeline": "/usr/local/bin/aliasdb_pipeline", "alncut": "/usr/local/bin/alncut", "alnpi": "/usr/local/bin/alnpi", "ar01_accret.py": "/usr/local/bin/ar01_accret.py", "bash": "/usr/local/bin/bash", "bashbug": "/usr/local/bin/bashbug", "batch_brb_functions.py": "/usr/local/bin/batch_brb_functions.py", "batch_brb_setup": "/usr/local/bin/batch_brb_setup", "batch_makeblastdb": "/usr/local/bin/batch_makeblastdb", "del01_delete_db_entries.py": "/usr/local/bin/del01_delete_db_entries.py", "delete_db": "/usr/local/bin/delete_db", "fascodon": "/usr/local/bin/fascodon", "fascomp": "/usr/local/bin/fascomp", "fasconvert": "/usr/local/bin/fasconvert", "fascut": "/usr/local/bin/fascut", "fasfilter": "/usr/local/bin/fasfilter", "fasgrep": "/usr/local/bin/fasgrep", "fashead": "/usr/local/bin/fashead", "faslen": "/usr/local/bin/faslen", "faspaste": "/usr/local/bin/faspaste", "fasrc": "/usr/local/bin/fasrc", "fassort": "/usr/local/bin/fassort", "fassub": "/usr/local/bin/fassub", "fastail": "/usr/local/bin/fastail", "fastax": "/usr/local/bin/fastax", "fastaxsort": "/usr/local/bin/fastaxsort", "fastr": "/usr/local/bin/fastr", "fasttree_pipeline": "/usr/local/bin/fasttree_pipeline", "fasuniq": "/usr/local/bin/fasuniq", "faswc": "/usr/local/bin/faswc", "fasxl": "/usr/local/bin/fasxl", "ft01_extract_accessions.py": "/usr/local/bin/ft01_extract_accessions.py", "gbfalncut": "/usr/local/bin/gbfalncut", "gbfcut": "/usr/local/bin/gbfcut", "mdb01_makeblastdb.sh": "/usr/local/bin/mdb01_makeblastdb.sh", "mdb02_convert_headers.py": "/usr/local/bin/mdb02_convert_headers.py", "mdb03_add_to_db.py": "/usr/local/bin/mdb03_add_to_db.py", "merge_results": "/usr/local/bin/merge_results", "or01_filter_hits.py": "/usr/local/bin/or01_filter_hits.py", "or02_find_orthologs.py": "/usr/local/bin/or02_find_orthologs.py", "orthology_pipeline": "/usr/local/bin/orthology_pipeline", "show": "/usr/local/bin/show", "seqkit": "/usr/local/bin/seqkit", "FastTree-2.1.10.c": "/usr/local/bin/FastTree-2.1.10.c", "FastTreeMP": "/usr/local/bin/FastTreeMP", "muscle": "/usr/local/bin/muscle", "FastTree": "/usr/local/bin/FastTree", "fasttree": "/usr/local/bin/fasttree", "CA.pm": "/usr/local/bin/CA.pm", "cacert.pem": "/usr/local/bin/cacert.pem", "index-themes": "/usr/local/bin/index-themes", "fetch-extras": "/usr/local/bin/fetch-extras"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/batch_brb.
shpc-registry automated BioContainers addition for batch_brb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/batch_brb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/batch_brb:1.0.1--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/batch_brb/1.0.1--hdfd78af_1
$ module help quay.io/biocontainers/batch_brb/1.0.1--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### batch_brb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### batch_brb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### batch_brb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### batch_brb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### batch_brb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### batch_brb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### accession_retrieve

```bash
$ singularity exec <container> /usr/local/bin/accession_retrieve
$ podman run --it --rm --entrypoint /usr/local/bin/accession_retrieve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accession_retrieve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adb01_check_db.py

```bash
$ singularity exec <container> /usr/local/bin/adb01_check_db.py
$ podman run --it --rm --entrypoint /usr/local/bin/adb01_check_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adb01_check_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adb02_add_alias_to_db.py

```bash
$ singularity exec <container> /usr/local/bin/adb02_add_alias_to_db.py
$ podman run --it --rm --entrypoint /usr/local/bin/adb02_add_alias_to_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adb02_add_alias_to_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aliasdb_pipeline

```bash
$ singularity exec <container> /usr/local/bin/aliasdb_pipeline
$ podman run --it --rm --entrypoint /usr/local/bin/aliasdb_pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aliasdb_pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alncut

```bash
$ singularity exec <container> /usr/local/bin/alncut
$ podman run --it --rm --entrypoint /usr/local/bin/alncut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alncut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alnpi

```bash
$ singularity exec <container> /usr/local/bin/alnpi
$ podman run --it --rm --entrypoint /usr/local/bin/alnpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alnpi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ar01_accret.py

```bash
$ singularity exec <container> /usr/local/bin/ar01_accret.py
$ podman run --it --rm --entrypoint /usr/local/bin/ar01_accret.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ar01_accret.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bash

```bash
$ singularity exec <container> /usr/local/bin/bash
$ podman run --it --rm --entrypoint /usr/local/bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bashbug

```bash
$ singularity exec <container> /usr/local/bin/bashbug
$ podman run --it --rm --entrypoint /usr/local/bin/bashbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bashbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### batch_brb_functions.py

```bash
$ singularity exec <container> /usr/local/bin/batch_brb_functions.py
$ podman run --it --rm --entrypoint /usr/local/bin/batch_brb_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/batch_brb_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### batch_brb_setup

```bash
$ singularity exec <container> /usr/local/bin/batch_brb_setup
$ podman run --it --rm --entrypoint /usr/local/bin/batch_brb_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/batch_brb_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### batch_makeblastdb

```bash
$ singularity exec <container> /usr/local/bin/batch_makeblastdb
$ podman run --it --rm --entrypoint /usr/local/bin/batch_makeblastdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/batch_makeblastdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### del01_delete_db_entries.py

```bash
$ singularity exec <container> /usr/local/bin/del01_delete_db_entries.py
$ podman run --it --rm --entrypoint /usr/local/bin/del01_delete_db_entries.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/del01_delete_db_entries.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delete_db

```bash
$ singularity exec <container> /usr/local/bin/delete_db
$ podman run --it --rm --entrypoint /usr/local/bin/delete_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delete_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fascodon

```bash
$ singularity exec <container> /usr/local/bin/fascodon
$ podman run --it --rm --entrypoint /usr/local/bin/fascodon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fascodon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fascomp

```bash
$ singularity exec <container> /usr/local/bin/fascomp
$ podman run --it --rm --entrypoint /usr/local/bin/fascomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fascomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasconvert

```bash
$ singularity exec <container> /usr/local/bin/fasconvert
$ podman run --it --rm --entrypoint /usr/local/bin/fasconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fascut

```bash
$ singularity exec <container> /usr/local/bin/fascut
$ podman run --it --rm --entrypoint /usr/local/bin/fascut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fascut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasfilter

```bash
$ singularity exec <container> /usr/local/bin/fasfilter
$ podman run --it --rm --entrypoint /usr/local/bin/fasfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasgrep

```bash
$ singularity exec <container> /usr/local/bin/fasgrep
$ podman run --it --rm --entrypoint /usr/local/bin/fasgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fashead

```bash
$ singularity exec <container> /usr/local/bin/fashead
$ podman run --it --rm --entrypoint /usr/local/bin/fashead   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fashead   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faslen

```bash
$ singularity exec <container> /usr/local/bin/faslen
$ podman run --it --rm --entrypoint /usr/local/bin/faslen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faslen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faspaste

```bash
$ singularity exec <container> /usr/local/bin/faspaste
$ podman run --it --rm --entrypoint /usr/local/bin/faspaste   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faspaste   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasrc

```bash
$ singularity exec <container> /usr/local/bin/fasrc
$ podman run --it --rm --entrypoint /usr/local/bin/fasrc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasrc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fassort

```bash
$ singularity exec <container> /usr/local/bin/fassort
$ podman run --it --rm --entrypoint /usr/local/bin/fassort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fassort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fassub

```bash
$ singularity exec <container> /usr/local/bin/fassub
$ podman run --it --rm --entrypoint /usr/local/bin/fassub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fassub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastail

```bash
$ singularity exec <container> /usr/local/bin/fastail
$ podman run --it --rm --entrypoint /usr/local/bin/fastail   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastail   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastax

```bash
$ singularity exec <container> /usr/local/bin/fastax
$ podman run --it --rm --entrypoint /usr/local/bin/fastax   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastax   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaxsort

```bash
$ singularity exec <container> /usr/local/bin/fastaxsort
$ podman run --it --rm --entrypoint /usr/local/bin/fastaxsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaxsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastr

```bash
$ singularity exec <container> /usr/local/bin/fastr
$ podman run --it --rm --entrypoint /usr/local/bin/fastr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasttree_pipeline

```bash
$ singularity exec <container> /usr/local/bin/fasttree_pipeline
$ podman run --it --rm --entrypoint /usr/local/bin/fasttree_pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasttree_pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasuniq

```bash
$ singularity exec <container> /usr/local/bin/fasuniq
$ podman run --it --rm --entrypoint /usr/local/bin/fasuniq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasuniq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faswc

```bash
$ singularity exec <container> /usr/local/bin/faswc
$ podman run --it --rm --entrypoint /usr/local/bin/faswc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faswc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasxl

```bash
$ singularity exec <container> /usr/local/bin/fasxl
$ podman run --it --rm --entrypoint /usr/local/bin/fasxl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasxl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ft01_extract_accessions.py

```bash
$ singularity exec <container> /usr/local/bin/ft01_extract_accessions.py
$ podman run --it --rm --entrypoint /usr/local/bin/ft01_extract_accessions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ft01_extract_accessions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbfalncut

```bash
$ singularity exec <container> /usr/local/bin/gbfalncut
$ podman run --it --rm --entrypoint /usr/local/bin/gbfalncut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbfalncut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbfcut

```bash
$ singularity exec <container> /usr/local/bin/gbfcut
$ podman run --it --rm --entrypoint /usr/local/bin/gbfcut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbfcut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mdb01_makeblastdb.sh

```bash
$ singularity exec <container> /usr/local/bin/mdb01_makeblastdb.sh
$ podman run --it --rm --entrypoint /usr/local/bin/mdb01_makeblastdb.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mdb01_makeblastdb.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mdb02_convert_headers.py

```bash
$ singularity exec <container> /usr/local/bin/mdb02_convert_headers.py
$ podman run --it --rm --entrypoint /usr/local/bin/mdb02_convert_headers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mdb02_convert_headers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mdb03_add_to_db.py

```bash
$ singularity exec <container> /usr/local/bin/mdb03_add_to_db.py
$ podman run --it --rm --entrypoint /usr/local/bin/mdb03_add_to_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mdb03_add_to_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_results

```bash
$ singularity exec <container> /usr/local/bin/merge_results
$ podman run --it --rm --entrypoint /usr/local/bin/merge_results   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_results   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### or01_filter_hits.py

```bash
$ singularity exec <container> /usr/local/bin/or01_filter_hits.py
$ podman run --it --rm --entrypoint /usr/local/bin/or01_filter_hits.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/or01_filter_hits.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### or02_find_orthologs.py

```bash
$ singularity exec <container> /usr/local/bin/or02_find_orthologs.py
$ podman run --it --rm --entrypoint /usr/local/bin/or02_find_orthologs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/or02_find_orthologs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthology_pipeline

```bash
$ singularity exec <container> /usr/local/bin/orthology_pipeline
$ podman run --it --rm --entrypoint /usr/local/bin/orthology_pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthology_pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### show

```bash
$ singularity exec <container> /usr/local/bin/show
$ podman run --it --rm --entrypoint /usr/local/bin/show   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/show   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqkit

```bash
$ singularity exec <container> /usr/local/bin/seqkit
$ podman run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree-2.1.10.c

```bash
$ singularity exec <container> /usr/local/bin/FastTree-2.1.10.c
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree-2.1.10.c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree-2.1.10.c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTreeMP

```bash
$ singularity exec <container> /usr/local/bin/FastTreeMP
$ podman run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### muscle

```bash
$ singularity exec <container> /usr/local/bin/muscle
$ podman run --it --rm --entrypoint /usr/local/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree

```bash
$ singularity exec <container> /usr/local/bin/FastTree
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasttree

```bash
$ singularity exec <container> /usr/local/bin/fasttree
$ podman run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CA.pm

```bash
$ singularity exec <container> /usr/local/bin/CA.pm
$ podman run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cacert.pem

```bash
$ singularity exec <container> /usr/local/bin/cacert.pem
$ podman run --it --rm --entrypoint /usr/local/bin/cacert.pem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cacert.pem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index-themes

```bash
$ singularity exec <container> /usr/local/bin/index-themes
$ podman run --it --rm --entrypoint /usr/local/bin/index-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch-extras

```bash
$ singularity exec <container> /usr/local/bin/fetch-extras
$ podman run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
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