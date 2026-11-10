#Requires -Version 5.1
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet(
        'architect',
        'implementer',
        'tester',
        'reviewer',
        'security-reviewer',
        'devops',
        'docs-writer',
        'orchestrator'
    )]
    [string]$Role,

    [Parameter(Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string]$Task,

    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$templatePath = Join-Path $repoRoot ".herdr\templates\gfm-$Role.md"

if (-not (Test-Path -LiteralPath $templatePath)) {
    throw "Template nao encontrado: $templatePath"
}

$text = [IO.File]::ReadAllText($templatePath, [Text.Encoding]::UTF8)
$normalized = $text -replace "`r`n", "`n"

if (-not $normalized.StartsWith("---`n")) {
    throw "Template sem frontmatter: $templatePath"
}

$end = $normalized.IndexOf("`n---", 4)
if ($end -lt 0) {
    throw "Frontmatter nao fechado: $templatePath"
}

$frontmatter = $normalized.Substring(4, $end - 4)
$body = $normalized.Substring($end + 4).Trim()
$command = $null

foreach ($line in $frontmatter -split "`n") {
    if ($line -match '^command:\s*(.+)$') {
        $command = $Matches[1].Trim()
        break
    }
}

if (-not $command) {
    throw "Template sem command: $templatePath"
}

if ($command -notmatch '^opencode\s+--agent\s+([a-z0-9-]+)$') {
    throw "Comando nao suportado por run-agent.ps1: $command"
}

$agent = $Matches[1]
if ($agent -ne $Role) {
    throw "Agente do template ($agent) diverge do papel solicitado ($Role)"
}

$opencode = Get-Command -Name opencode -ErrorAction SilentlyContinue
if (-not $opencode) {
    throw "opencode nao encontrado no PATH"
}

$primaryRoles = @('architect', 'implementer', 'devops', 'orchestrator')
if ($Role -notin $primaryRoles) {
    Write-Warning "OpenCode 1.19.0 executa '$Role' no agente padrao; subagente nao e selecionavel via CLI."
}

$prompt = $body + "`n`nTarefa:`n`n" + $Task.Trim()

if ($DryRun) {
    Write-Output "opencode run --agent $agent <prompt>"
    return
}

& $opencode.Source run --agent $agent $prompt
exit $LASTEXITCODE
