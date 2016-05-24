package br.jus.tse.eleitoral.eleitor.dominio.infra.daos;

import br.jus.tse.corporativa.arqjeespring.infra.daos.IBaseCRUDDAO;
import br.jus.tse.corporativa.arqjeespring.infra.exceptions.DBAcessoDadosException;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.ViewLocalVotacaoTemporario;

public interface IViewLocalVotacaoTemporarioDAO extends IBaseCRUDDAO<ViewLocalVotacaoTemporario, String> {

	public ViewLocalVotacaoTemporario findByCodObjetoEleitor(String id) throws DBAcessoDadosException;
	
}
