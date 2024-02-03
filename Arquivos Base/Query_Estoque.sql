SELECT
    lgpla   AS posicao,
    lgtyp   AS tipo,
    huident AS hu,
    matid   AS id_material,
    quan    AS qtd
FROM
    mard_dali_ewm.scwm_aqua_pl7
WHERE
        lgnum = 'BR01'
    AND lgtyp NOT IN ( '9010', '9020', '9030', '9100', '9070',
                       '9060', '8010', '8020', '8030', '8040',
                       '8042', '8041', '8000', '1001', ' ',
                       '8050', 'BM99', 'PM99', 'PM05', 'BM04',
                       'PANA', '9050', 'PM07' );