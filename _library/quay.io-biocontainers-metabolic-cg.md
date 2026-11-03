---
layout: container
name:  "quay.io/biocontainers/metabolic-cg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metabolic-cg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metabolic-cg/container.yaml"
updated_at: "2026-11-03 06:29:12.679978"
latest: "4.1.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/metabolic-cg"
aliases:
 - "All_Module_KO_ids.txt"
 - "METABOLIC-C.2nd_run.pl"
 - "METABOLIC-C.pl"
 - "METABOLIC-G.pl"
 - "METABOLIC_hmm_db.tgz"
 - "METABOLIC_template_and_database.tgz"
 - "coverm"
 - "create_excel_spreadsheet.R"
 - "draw_biogeochemical_cycles.R"
 - "draw_functional_network_diagram.R"
 - "draw_metabolic_Sankey_diagram.R"
 - "draw_sequential_reaction_diagram.R"
 - "gmake"
 - "idle3.15"
 - "pydoc3.15"
 - "python3.15"
 - "python3.15-config"
 - "strobealign"
 - "skani"
 - "gawk-5.4.1"
 - "starcode"
 - "sambamba"
 - "seq_cache_populate.py"
 - "zless"
 - "egrep"
 - "fgrep"
 - "grep"
 - "fastANI"
 - "gunzip"
 - "gzexe"
 - "gzip"
 - "uncompress"
 - "zcat"
 - "zcmp"
 - "zdiff"
 - "zegrep"
 - "zfgrep"
 - "zforce"
 - "zgrep"
 - "zmore"
 - "znew"
 - "bp_aacomp"
 - "bp_bioflat_index"
versions:
 - "4.1.1--hdfd78af_0"
description: "singularity registry hpc automated addition for metabolic-cg"
config: {"url": "https://biocontainers.pro/tools/metabolic-cg", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metabolic-cg", "latest": {"4.1.1--hdfd78af_0": "sha256:108374ed932a5d5e2116beea3cc7aed0b81c7f6669e94e618f55f834debc5b2b"}, "tags": {"4.1.1--hdfd78af_0": "sha256:108374ed932a5d5e2116beea3cc7aed0b81c7f6669e94e618f55f834debc5b2b"}, "docker": "quay.io/biocontainers/metabolic-cg", "aliases": {"All_Module_KO_ids.txt": "/usr/local/bin/All_Module_KO_ids.txt", "METABOLIC-C.2nd_run.pl": "/usr/local/bin/METABOLIC-C.2nd_run.pl", "METABOLIC-C.pl": "/usr/local/bin/METABOLIC-C.pl", "METABOLIC-G.pl": "/usr/local/bin/METABOLIC-G.pl", "METABOLIC_hmm_db.tgz": "/usr/local/bin/METABOLIC_hmm_db.tgz", "METABOLIC_template_and_database.tgz": "/usr/local/bin/METABOLIC_template_and_database.tgz", "coverm": "/usr/local/bin/coverm", "create_excel_spreadsheet.R": "/usr/local/bin/create_excel_spreadsheet.R", "draw_biogeochemical_cycles.R": "/usr/local/bin/draw_biogeochemical_cycles.R", "draw_functional_network_diagram.R": "/usr/local/bin/draw_functional_network_diagram.R", "draw_metabolic_Sankey_diagram.R": "/usr/local/bin/draw_metabolic_Sankey_diagram.R", "draw_sequential_reaction_diagram.R": "/usr/local/bin/draw_sequential_reaction_diagram.R", "gmake": "/usr/local/bin/gmake", "idle3.15": "/usr/local/bin/idle3.15", "pydoc3.15": "/usr/local/bin/pydoc3.15", "python3.15": "/usr/local/bin/python3.15", "python3.15-config": "/usr/local/bin/python3.15-config", "strobealign": "/usr/local/bin/strobealign", "skani": "/usr/local/bin/skani", "gawk-5.4.1": "/usr/local/bin/gawk-5.4.1", "starcode": "/usr/local/bin/starcode", "sambamba": "/usr/local/bin/sambamba", "seq_cache_populate.py": "/usr/local/bin/seq_cache_populate.py", "zless": "/usr/local/bin/zless", "egrep": "/usr/local/bin/egrep", "fgrep": "/usr/local/bin/fgrep", "grep": "/usr/local/bin/grep", "fastANI": "/usr/local/bin/fastANI", "gunzip": "/usr/local/bin/gunzip", "gzexe": "/usr/local/bin/gzexe", "gzip": "/usr/local/bin/gzip", "uncompress": "/usr/local/bin/uncompress", "zcat": "/usr/local/bin/zcat", "zcmp": "/usr/local/bin/zcmp", "zdiff": "/usr/local/bin/zdiff", "zegrep": "/usr/local/bin/zegrep", "zfgrep": "/usr/local/bin/zfgrep", "zforce": "/usr/local/bin/zforce", "zgrep": "/usr/local/bin/zgrep", "zmore": "/usr/local/bin/zmore", "znew": "/usr/local/bin/znew", "bp_aacomp": "/usr/local/bin/bp_aacomp", "bp_bioflat_index": "/usr/local/bin/bp_bioflat_index"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metabolic-cg.
singularity registry hpc automated addition for metabolic-cg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metabolic-cg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metabolic-cg:4.1.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metabolic-cg/4.1.1--hdfd78af_0
$ module help quay.io/biocontainers/metabolic-cg/4.1.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metabolic-cg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metabolic-cg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metabolic-cg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metabolic-cg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metabolic-cg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metabolic-cg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### All_Module_KO_ids.txt

```bash
$ singularity exec <container> /usr/local/bin/All_Module_KO_ids.txt
$ podman run --it --rm --entrypoint /usr/local/bin/All_Module_KO_ids.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/All_Module_KO_ids.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### METABOLIC-C.2nd_run.pl

```bash
$ singularity exec <container> /usr/local/bin/METABOLIC-C.2nd_run.pl
$ podman run --it --rm --entrypoint /usr/local/bin/METABOLIC-C.2nd_run.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/METABOLIC-C.2nd_run.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### METABOLIC-C.pl

```bash
$ singularity exec <container> /usr/local/bin/METABOLIC-C.pl
$ podman run --it --rm --entrypoint /usr/local/bin/METABOLIC-C.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/METABOLIC-C.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### METABOLIC-G.pl

```bash
$ singularity exec <container> /usr/local/bin/METABOLIC-G.pl
$ podman run --it --rm --entrypoint /usr/local/bin/METABOLIC-G.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/METABOLIC-G.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### METABOLIC_hmm_db.tgz

```bash
$ singularity exec <container> /usr/local/bin/METABOLIC_hmm_db.tgz
$ podman run --it --rm --entrypoint /usr/local/bin/METABOLIC_hmm_db.tgz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/METABOLIC_hmm_db.tgz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### METABOLIC_template_and_database.tgz

```bash
$ singularity exec <container> /usr/local/bin/METABOLIC_template_and_database.tgz
$ podman run --it --rm --entrypoint /usr/local/bin/METABOLIC_template_and_database.tgz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/METABOLIC_template_and_database.tgz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverm

```bash
$ singularity exec <container> /usr/local/bin/coverm
$ podman run --it --rm --entrypoint /usr/local/bin/coverm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_excel_spreadsheet.R

```bash
$ singularity exec <container> /usr/local/bin/create_excel_spreadsheet.R
$ podman run --it --rm --entrypoint /usr/local/bin/create_excel_spreadsheet.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_excel_spreadsheet.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### draw_biogeochemical_cycles.R

```bash
$ singularity exec <container> /usr/local/bin/draw_biogeochemical_cycles.R
$ podman run --it --rm --entrypoint /usr/local/bin/draw_biogeochemical_cycles.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/draw_biogeochemical_cycles.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### draw_functional_network_diagram.R

```bash
$ singularity exec <container> /usr/local/bin/draw_functional_network_diagram.R
$ podman run --it --rm --entrypoint /usr/local/bin/draw_functional_network_diagram.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/draw_functional_network_diagram.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### draw_metabolic_Sankey_diagram.R

```bash
$ singularity exec <container> /usr/local/bin/draw_metabolic_Sankey_diagram.R
$ podman run --it --rm --entrypoint /usr/local/bin/draw_metabolic_Sankey_diagram.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/draw_metabolic_Sankey_diagram.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### draw_sequential_reaction_diagram.R

```bash
$ singularity exec <container> /usr/local/bin/draw_sequential_reaction_diagram.R
$ podman run --it --rm --entrypoint /usr/local/bin/draw_sequential_reaction_diagram.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/draw_sequential_reaction_diagram.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmake

```bash
$ singularity exec <container> /usr/local/bin/gmake
$ podman run --it --rm --entrypoint /usr/local/bin/gmake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.15

```bash
$ singularity exec <container> /usr/local/bin/idle3.15
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.15

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.15
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.15

```bash
$ singularity exec <container> /usr/local/bin/python3.15
$ podman run --it --rm --entrypoint /usr/local/bin/python3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.15-config

```bash
$ singularity exec <container> /usr/local/bin/python3.15-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.15-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.15-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strobealign

```bash
$ singularity exec <container> /usr/local/bin/strobealign
$ podman run --it --rm --entrypoint /usr/local/bin/strobealign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strobealign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skani

```bash
$ singularity exec <container> /usr/local/bin/skani
$ podman run --it --rm --entrypoint /usr/local/bin/skani   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skani   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.4.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.4.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starcode

```bash
$ singularity exec <container> /usr/local/bin/starcode
$ podman run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sambamba

```bash
$ singularity exec <container> /usr/local/bin/sambamba
$ podman run --it --rm --entrypoint /usr/local/bin/sambamba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sambamba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq_cache_populate.py

```bash
$ singularity exec <container> /usr/local/bin/seq_cache_populate.py
$ podman run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zless

```bash
$ singularity exec <container> /usr/local/bin/zless
$ podman run --it --rm --entrypoint /usr/local/bin/zless   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zless   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### egrep

```bash
$ singularity exec <container> /usr/local/bin/egrep
$ podman run --it --rm --entrypoint /usr/local/bin/egrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/egrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fgrep

```bash
$ singularity exec <container> /usr/local/bin/fgrep
$ podman run --it --rm --entrypoint /usr/local/bin/fgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grep

```bash
$ singularity exec <container> /usr/local/bin/grep
$ podman run --it --rm --entrypoint /usr/local/bin/grep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastANI

```bash
$ singularity exec <container> /usr/local/bin/fastANI
$ podman run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gunzip

```bash
$ singularity exec <container> /usr/local/bin/gunzip
$ podman run --it --rm --entrypoint /usr/local/bin/gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gzexe

```bash
$ singularity exec <container> /usr/local/bin/gzexe
$ podman run --it --rm --entrypoint /usr/local/bin/gzexe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gzexe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gzip

```bash
$ singularity exec <container> /usr/local/bin/gzip
$ podman run --it --rm --entrypoint /usr/local/bin/gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uncompress

```bash
$ singularity exec <container> /usr/local/bin/uncompress
$ podman run --it --rm --entrypoint /usr/local/bin/uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zcat

```bash
$ singularity exec <container> /usr/local/bin/zcat
$ podman run --it --rm --entrypoint /usr/local/bin/zcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zcmp

```bash
$ singularity exec <container> /usr/local/bin/zcmp
$ podman run --it --rm --entrypoint /usr/local/bin/zcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zdiff

```bash
$ singularity exec <container> /usr/local/bin/zdiff
$ podman run --it --rm --entrypoint /usr/local/bin/zdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zegrep

```bash
$ singularity exec <container> /usr/local/bin/zegrep
$ podman run --it --rm --entrypoint /usr/local/bin/zegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zfgrep

```bash
$ singularity exec <container> /usr/local/bin/zfgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zforce

```bash
$ singularity exec <container> /usr/local/bin/zforce
$ podman run --it --rm --entrypoint /usr/local/bin/zforce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zforce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zgrep

```bash
$ singularity exec <container> /usr/local/bin/zgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zmore

```bash
$ singularity exec <container> /usr/local/bin/zmore
$ podman run --it --rm --entrypoint /usr/local/bin/zmore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zmore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### znew

```bash
$ singularity exec <container> /usr/local/bin/znew
$ podman run --it --rm --entrypoint /usr/local/bin/znew   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/znew   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_aacomp

```bash
$ singularity exec <container> /usr/local/bin/bp_aacomp
$ podman run --it --rm --entrypoint /usr/local/bin/bp_aacomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_aacomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_bioflat_index

```bash
$ singularity exec <container> /usr/local/bin/bp_bioflat_index
$ podman run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index   -v ${PWD} -w ${PWD} <container> -c " $@"
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