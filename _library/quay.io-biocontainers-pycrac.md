---
layout: container
name:  "quay.io/biocontainers/pycrac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pycrac/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pycrac/container.yaml"
updated_at: "2023-07-08 03:45:11.022592"
latest: "1.5.2--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/pycrac"
aliases:
 - "pyAlignment2Tab.py"
 - "pyBarcodeFilter.py"
 - "pyBinCollector.py"
 - "pyCalculateChromosomeLengths.py"
 - "pyCalculateFDRs.py"
 - "pyCalculateMutationFrequencies.py"
 - "pyCheckGTFfile.py"
 - "pyClusterReads.py"
 - "pyExtractLinesFromGTF.py"
 - "pyFasta2tab.py"
 - "pyFastqDuplicateRemover.py"
 - "pyFastqJoiner.py"
 - "pyFastqSplitter.py"
 - "pyFilterGTF.py"
 - "pyGTF2bed.py"
 - "pyGTF2bedGraph.py"
 - "pyGTF2sgr.py"
 - "pyGetGTFSources.py"
 - "pyGetGeneNamesFromGTF.py"
 - "pyMotif.py"
 - "pyNormalizeIntervalLengths.py"
 - "pyPileup.py"
 - "pyReadAligner.py"
 - "pyReadCounters.py"
 - "pySelectMotifsFromGTF.py"
 - "pybed2GTF.py"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "1.5.1--pyh5e36f6f_0"
 - "1.5.2--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for pycrac"
config: {"url": "https://biocontainers.pro/tools/pycrac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pycrac", "latest": {"1.5.2--pyh7cba7a3_0": "sha256:6a91970da6caa9ea4fc46d27892217fb4f756a44115d33158d9b1a7b5658d75f"}, "tags": {"1.5.1--pyh5e36f6f_0": "sha256:ecd1d27d5e584a550ffd28c6bdae218e00c8d9defeea453c68f8762be0ecf2f9", "1.5.2--pyh7cba7a3_0": "sha256:6a91970da6caa9ea4fc46d27892217fb4f756a44115d33158d9b1a7b5658d75f"}, "docker": "quay.io/biocontainers/pycrac", "aliases": {"pyAlignment2Tab.py": "/usr/local/bin/pyAlignment2Tab.py", "pyBarcodeFilter.py": "/usr/local/bin/pyBarcodeFilter.py", "pyBinCollector.py": "/usr/local/bin/pyBinCollector.py", "pyCalculateChromosomeLengths.py": "/usr/local/bin/pyCalculateChromosomeLengths.py", "pyCalculateFDRs.py": "/usr/local/bin/pyCalculateFDRs.py", "pyCalculateMutationFrequencies.py": "/usr/local/bin/pyCalculateMutationFrequencies.py", "pyCheckGTFfile.py": "/usr/local/bin/pyCheckGTFfile.py", "pyClusterReads.py": "/usr/local/bin/pyClusterReads.py", "pyExtractLinesFromGTF.py": "/usr/local/bin/pyExtractLinesFromGTF.py", "pyFasta2tab.py": "/usr/local/bin/pyFasta2tab.py", "pyFastqDuplicateRemover.py": "/usr/local/bin/pyFastqDuplicateRemover.py", "pyFastqJoiner.py": "/usr/local/bin/pyFastqJoiner.py", "pyFastqSplitter.py": "/usr/local/bin/pyFastqSplitter.py", "pyFilterGTF.py": "/usr/local/bin/pyFilterGTF.py", "pyGTF2bed.py": "/usr/local/bin/pyGTF2bed.py", "pyGTF2bedGraph.py": "/usr/local/bin/pyGTF2bedGraph.py", "pyGTF2sgr.py": "/usr/local/bin/pyGTF2sgr.py", "pyGetGTFSources.py": "/usr/local/bin/pyGetGTFSources.py", "pyGetGeneNamesFromGTF.py": "/usr/local/bin/pyGetGeneNamesFromGTF.py", "pyMotif.py": "/usr/local/bin/pyMotif.py", "pyNormalizeIntervalLengths.py": "/usr/local/bin/pyNormalizeIntervalLengths.py", "pyPileup.py": "/usr/local/bin/pyPileup.py", "pyReadAligner.py": "/usr/local/bin/pyReadAligner.py", "pyReadCounters.py": "/usr/local/bin/pyReadCounters.py", "pySelectMotifsFromGTF.py": "/usr/local/bin/pySelectMotifsFromGTF.py", "pybed2GTF.py": "/usr/local/bin/pybed2GTF.py", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pycrac.
shpc-registry automated BioContainers addition for pycrac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pycrac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pycrac:1.5.2--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pycrac/1.5.2--pyh7cba7a3_0
$ module help quay.io/biocontainers/pycrac/1.5.2--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pycrac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pycrac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pycrac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pycrac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pycrac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pycrac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pyAlignment2Tab.py

```bash
$ singularity exec <container> /usr/local/bin/pyAlignment2Tab.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyAlignment2Tab.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyAlignment2Tab.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyBarcodeFilter.py

```bash
$ singularity exec <container> /usr/local/bin/pyBarcodeFilter.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyBarcodeFilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyBarcodeFilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyBinCollector.py

```bash
$ singularity exec <container> /usr/local/bin/pyBinCollector.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyBinCollector.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyBinCollector.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyCalculateChromosomeLengths.py

```bash
$ singularity exec <container> /usr/local/bin/pyCalculateChromosomeLengths.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyCalculateChromosomeLengths.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyCalculateChromosomeLengths.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyCalculateFDRs.py

```bash
$ singularity exec <container> /usr/local/bin/pyCalculateFDRs.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyCalculateFDRs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyCalculateFDRs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyCalculateMutationFrequencies.py

```bash
$ singularity exec <container> /usr/local/bin/pyCalculateMutationFrequencies.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyCalculateMutationFrequencies.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyCalculateMutationFrequencies.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyCheckGTFfile.py

```bash
$ singularity exec <container> /usr/local/bin/pyCheckGTFfile.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyCheckGTFfile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyCheckGTFfile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyClusterReads.py

```bash
$ singularity exec <container> /usr/local/bin/pyClusterReads.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyClusterReads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyClusterReads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyExtractLinesFromGTF.py

```bash
$ singularity exec <container> /usr/local/bin/pyExtractLinesFromGTF.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyExtractLinesFromGTF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyExtractLinesFromGTF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyFasta2tab.py

```bash
$ singularity exec <container> /usr/local/bin/pyFasta2tab.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyFasta2tab.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyFasta2tab.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyFastqDuplicateRemover.py

```bash
$ singularity exec <container> /usr/local/bin/pyFastqDuplicateRemover.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyFastqDuplicateRemover.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyFastqDuplicateRemover.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyFastqJoiner.py

```bash
$ singularity exec <container> /usr/local/bin/pyFastqJoiner.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyFastqJoiner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyFastqJoiner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyFastqSplitter.py

```bash
$ singularity exec <container> /usr/local/bin/pyFastqSplitter.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyFastqSplitter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyFastqSplitter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyFilterGTF.py

```bash
$ singularity exec <container> /usr/local/bin/pyFilterGTF.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyFilterGTF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyFilterGTF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyGTF2bed.py

```bash
$ singularity exec <container> /usr/local/bin/pyGTF2bed.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyGTF2bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyGTF2bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyGTF2bedGraph.py

```bash
$ singularity exec <container> /usr/local/bin/pyGTF2bedGraph.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyGTF2bedGraph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyGTF2bedGraph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyGTF2sgr.py

```bash
$ singularity exec <container> /usr/local/bin/pyGTF2sgr.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyGTF2sgr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyGTF2sgr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyGetGTFSources.py

```bash
$ singularity exec <container> /usr/local/bin/pyGetGTFSources.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyGetGTFSources.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyGetGTFSources.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyGetGeneNamesFromGTF.py

```bash
$ singularity exec <container> /usr/local/bin/pyGetGeneNamesFromGTF.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyGetGeneNamesFromGTF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyGetGeneNamesFromGTF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyMotif.py

```bash
$ singularity exec <container> /usr/local/bin/pyMotif.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyMotif.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyMotif.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyNormalizeIntervalLengths.py

```bash
$ singularity exec <container> /usr/local/bin/pyNormalizeIntervalLengths.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyNormalizeIntervalLengths.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyNormalizeIntervalLengths.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyPileup.py

```bash
$ singularity exec <container> /usr/local/bin/pyPileup.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyPileup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyPileup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyReadAligner.py

```bash
$ singularity exec <container> /usr/local/bin/pyReadAligner.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyReadAligner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyReadAligner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyReadCounters.py

```bash
$ singularity exec <container> /usr/local/bin/pyReadCounters.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyReadCounters.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyReadCounters.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pySelectMotifsFromGTF.py

```bash
$ singularity exec <container> /usr/local/bin/pySelectMotifsFromGTF.py
$ podman run --it --rm --entrypoint /usr/local/bin/pySelectMotifsFromGTF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pySelectMotifsFromGTF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybed2GTF.py

```bash
$ singularity exec <container> /usr/local/bin/pybed2GTF.py
$ podman run --it --rm --entrypoint /usr/local/bin/pybed2GTF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybed2GTF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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