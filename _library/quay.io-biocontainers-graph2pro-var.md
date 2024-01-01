---
layout: container
name:  "quay.io/biocontainers/graph2pro-var"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/graph2pro-var/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/graph2pro-var/container.yaml"
updated_at: "2024-01-01 03:32:26.343725"
latest: "1.0.0--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/graph2pro-var"
aliases:
 - "DBGraph2Pro"
 - "DBGraphPep2Pro"
 - "FragGeneScan"
 - "combineFragandDBGraph_fastg.py"
 - "combineFragandDBGraph_fastg_old.py"
 - "combineSpec_files.py"
 - "combineThree_o.py"
 - "createFixedReverseKR.py"
 - "fastg2fasta.py"
 - "generate_var2pep_only.py"
 - "getProteinFasta.py"
 - "getUniquePeptides_files.py"
 - "getUniqueProtein_o.py"
 - "msgf_plus"
 - "parseFDR_o.py"
 - "parseFDR_o_peptide.py"
 - "parseMismatch.py"
 - "patchpos.py"
 - "prerapsearch"
 - "rapsearch"
 - "removeRC.py"
 - "replaceID.py"
 - "run_FragGeneScan.pl"
 - "step1output.py"
 - "tryptic.py"
 - "FET.pl"
 - "cd-hit-clstr_2_blm8.pl"
 - "clstr_list.pl"
 - "clstr_list_sort.pl"
 - "cd-hit"
 - "cd-hit-2d"
 - "cd-hit-2d-para.pl"
 - "cd-hit-454"
 - "cd-hit-div"
 - "cd-hit-div.pl"
versions:
 - "1.0.0--h9ee0642_1"
description: "shpc-registry automated BioContainers addition for graph2pro-var"
config: {"url": "https://biocontainers.pro/tools/graph2pro-var", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for graph2pro-var", "latest": {"1.0.0--h9ee0642_1": "sha256:7c3c490d2ca932be14e3a49a8d706bdd9c0db64a0be8f422bc2b0b7baaaa5e25"}, "tags": {"1.0.0--h9ee0642_1": "sha256:7c3c490d2ca932be14e3a49a8d706bdd9c0db64a0be8f422bc2b0b7baaaa5e25"}, "docker": "quay.io/biocontainers/graph2pro-var", "aliases": {"DBGraph2Pro": "/usr/local/bin/DBGraph2Pro", "DBGraphPep2Pro": "/usr/local/bin/DBGraphPep2Pro", "FragGeneScan": "/usr/local/bin/FragGeneScan", "combineFragandDBGraph_fastg.py": "/usr/local/bin/combineFragandDBGraph_fastg.py", "combineFragandDBGraph_fastg_old.py": "/usr/local/bin/combineFragandDBGraph_fastg_old.py", "combineSpec_files.py": "/usr/local/bin/combineSpec_files.py", "combineThree_o.py": "/usr/local/bin/combineThree_o.py", "createFixedReverseKR.py": "/usr/local/bin/createFixedReverseKR.py", "fastg2fasta.py": "/usr/local/bin/fastg2fasta.py", "generate_var2pep_only.py": "/usr/local/bin/generate_var2pep_only.py", "getProteinFasta.py": "/usr/local/bin/getProteinFasta.py", "getUniquePeptides_files.py": "/usr/local/bin/getUniquePeptides_files.py", "getUniqueProtein_o.py": "/usr/local/bin/getUniqueProtein_o.py", "msgf_plus": "/usr/local/bin/msgf_plus", "parseFDR_o.py": "/usr/local/bin/parseFDR_o.py", "parseFDR_o_peptide.py": "/usr/local/bin/parseFDR_o_peptide.py", "parseMismatch.py": "/usr/local/bin/parseMismatch.py", "patchpos.py": "/usr/local/bin/patchpos.py", "prerapsearch": "/usr/local/bin/prerapsearch", "rapsearch": "/usr/local/bin/rapsearch", "removeRC.py": "/usr/local/bin/removeRC.py", "replaceID.py": "/usr/local/bin/replaceID.py", "run_FragGeneScan.pl": "/usr/local/bin/run_FragGeneScan.pl", "step1output.py": "/usr/local/bin/step1output.py", "tryptic.py": "/usr/local/bin/tryptic.py", "FET.pl": "/usr/local/bin/FET.pl", "cd-hit-clstr_2_blm8.pl": "/usr/local/bin/cd-hit-clstr_2_blm8.pl", "clstr_list.pl": "/usr/local/bin/clstr_list.pl", "clstr_list_sort.pl": "/usr/local/bin/clstr_list_sort.pl", "cd-hit": "/usr/local/bin/cd-hit", "cd-hit-2d": "/usr/local/bin/cd-hit-2d", "cd-hit-2d-para.pl": "/usr/local/bin/cd-hit-2d-para.pl", "cd-hit-454": "/usr/local/bin/cd-hit-454", "cd-hit-div": "/usr/local/bin/cd-hit-div", "cd-hit-div.pl": "/usr/local/bin/cd-hit-div.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/graph2pro-var.
shpc-registry automated BioContainers addition for graph2pro-var
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/graph2pro-var
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/graph2pro-var:1.0.0--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/graph2pro-var/1.0.0--h9ee0642_1
$ module help quay.io/biocontainers/graph2pro-var/1.0.0--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### graph2pro-var-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### graph2pro-var-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### graph2pro-var-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### graph2pro-var-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### graph2pro-var-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### graph2pro-var-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### DBGraph2Pro

```bash
$ singularity exec <container> /usr/local/bin/DBGraph2Pro
$ podman run --it --rm --entrypoint /usr/local/bin/DBGraph2Pro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DBGraph2Pro   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DBGraphPep2Pro

```bash
$ singularity exec <container> /usr/local/bin/DBGraphPep2Pro
$ podman run --it --rm --entrypoint /usr/local/bin/DBGraphPep2Pro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DBGraphPep2Pro   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FragGeneScan

```bash
$ singularity exec <container> /usr/local/bin/FragGeneScan
$ podman run --it --rm --entrypoint /usr/local/bin/FragGeneScan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FragGeneScan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineFragandDBGraph_fastg.py

```bash
$ singularity exec <container> /usr/local/bin/combineFragandDBGraph_fastg.py
$ podman run --it --rm --entrypoint /usr/local/bin/combineFragandDBGraph_fastg.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineFragandDBGraph_fastg.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineFragandDBGraph_fastg_old.py

```bash
$ singularity exec <container> /usr/local/bin/combineFragandDBGraph_fastg_old.py
$ podman run --it --rm --entrypoint /usr/local/bin/combineFragandDBGraph_fastg_old.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineFragandDBGraph_fastg_old.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineSpec_files.py

```bash
$ singularity exec <container> /usr/local/bin/combineSpec_files.py
$ podman run --it --rm --entrypoint /usr/local/bin/combineSpec_files.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineSpec_files.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineThree_o.py

```bash
$ singularity exec <container> /usr/local/bin/combineThree_o.py
$ podman run --it --rm --entrypoint /usr/local/bin/combineThree_o.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineThree_o.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createFixedReverseKR.py

```bash
$ singularity exec <container> /usr/local/bin/createFixedReverseKR.py
$ podman run --it --rm --entrypoint /usr/local/bin/createFixedReverseKR.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/createFixedReverseKR.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastg2fasta.py

```bash
$ singularity exec <container> /usr/local/bin/fastg2fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/fastg2fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastg2fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_var2pep_only.py

```bash
$ singularity exec <container> /usr/local/bin/generate_var2pep_only.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_var2pep_only.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_var2pep_only.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getProteinFasta.py

```bash
$ singularity exec <container> /usr/local/bin/getProteinFasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/getProteinFasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getProteinFasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getUniquePeptides_files.py

```bash
$ singularity exec <container> /usr/local/bin/getUniquePeptides_files.py
$ podman run --it --rm --entrypoint /usr/local/bin/getUniquePeptides_files.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getUniquePeptides_files.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getUniqueProtein_o.py

```bash
$ singularity exec <container> /usr/local/bin/getUniqueProtein_o.py
$ podman run --it --rm --entrypoint /usr/local/bin/getUniqueProtein_o.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getUniqueProtein_o.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msgf_plus

```bash
$ singularity exec <container> /usr/local/bin/msgf_plus
$ podman run --it --rm --entrypoint /usr/local/bin/msgf_plus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msgf_plus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parseFDR_o.py

```bash
$ singularity exec <container> /usr/local/bin/parseFDR_o.py
$ podman run --it --rm --entrypoint /usr/local/bin/parseFDR_o.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parseFDR_o.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parseFDR_o_peptide.py

```bash
$ singularity exec <container> /usr/local/bin/parseFDR_o_peptide.py
$ podman run --it --rm --entrypoint /usr/local/bin/parseFDR_o_peptide.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parseFDR_o_peptide.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parseMismatch.py

```bash
$ singularity exec <container> /usr/local/bin/parseMismatch.py
$ podman run --it --rm --entrypoint /usr/local/bin/parseMismatch.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parseMismatch.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### patchpos.py

```bash
$ singularity exec <container> /usr/local/bin/patchpos.py
$ podman run --it --rm --entrypoint /usr/local/bin/patchpos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/patchpos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prerapsearch

```bash
$ singularity exec <container> /usr/local/bin/prerapsearch
$ podman run --it --rm --entrypoint /usr/local/bin/prerapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prerapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rapsearch

```bash
$ singularity exec <container> /usr/local/bin/rapsearch
$ podman run --it --rm --entrypoint /usr/local/bin/rapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### removeRC.py

```bash
$ singularity exec <container> /usr/local/bin/removeRC.py
$ podman run --it --rm --entrypoint /usr/local/bin/removeRC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/removeRC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### replaceID.py

```bash
$ singularity exec <container> /usr/local/bin/replaceID.py
$ podman run --it --rm --entrypoint /usr/local/bin/replaceID.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/replaceID.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_FragGeneScan.pl

```bash
$ singularity exec <container> /usr/local/bin/run_FragGeneScan.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run_FragGeneScan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_FragGeneScan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### step1output.py

```bash
$ singularity exec <container> /usr/local/bin/step1output.py
$ podman run --it --rm --entrypoint /usr/local/bin/step1output.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/step1output.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tryptic.py

```bash
$ singularity exec <container> /usr/local/bin/tryptic.py
$ podman run --it --rm --entrypoint /usr/local/bin/tryptic.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tryptic.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FET.pl

```bash
$ singularity exec <container> /usr/local/bin/FET.pl
$ podman run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-clstr_2_blm8.pl

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-clstr_2_blm8.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-clstr_2_blm8.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-clstr_2_blm8.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_list.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_list.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_list.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_list.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_list_sort.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_list_sort.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_list_sort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_list_sort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit

```bash
$ singularity exec <container> /usr/local/bin/cd-hit
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-2d

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-2d
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-2d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-2d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-2d-para.pl

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-2d-para.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-2d-para.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-2d-para.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-454

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-454
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-454   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-454   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-div

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-div
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-div   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-div   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-div.pl

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-div.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-div.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-div.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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