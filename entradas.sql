CREATE TABLE `entradas` (
  `id` int(11) NOT NULL,
  `nome` varchar(200) CHARACTER SET latin1 NOT NULL DEFAULT '',
  `entrada` varchar(955) CHARACTER SET latin1 NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci COMMENT='InnoDB free: 77824 kB';

INSERT INTO `entradas` (`id`, `nome`, `entrada`) VALUES
(325, 'Michael Sants', '2022-05-10 10:03:54.166327'),
(326, 'Nelson Mandela', '2022-05-10 10:03:54.166327');

ALTER TABLE `entradas`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `entradas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;
