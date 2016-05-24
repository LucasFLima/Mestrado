package br.jus.tse.eleitoral.eleitor.dominio.infra.daos.jpa;

import org.springframework.stereotype.Repository;

import br.jus.tse.corporativa.arqjeespring.infra.daos.jpa.AbstractBaseCRUDDAOJPA;
import br.jus.tse.corporativa.arqjeespring.infra.exceptions.DBAcessoDadosException;
import br.jus.tse.corporativa.arqjeespring.infra.exceptions.DBRecuperacaoDadosException;
import br.jus.tse.eleitoral.eleitor.dominio.infra.daos.IViewLocalVotacaoTemporarioDAO;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.ViewLocalVotacaoTemporario;

@Repository
public class ViewLocalVotacaoTemporarioDAOJPA 
	 extends AbstractBaseCRUDDAOJPA<ViewLocalVotacaoTemporario, String> 
  implements IViewLocalVotacaoTemporarioDAO {

	
	public ViewLocalVotacaoTemporarioDAOJPA() {
		
	}
	
	
	@Override
	protected Class<ViewLocalVotacaoTemporario> getEntityClass() {
		return ViewLocalVotacaoTemporario.class;
	}

	
	@Override
	public ViewLocalVotacaoTemporario findByCodObjetoEleitor(String id) throws DBAcessoDadosException {

		ViewLocalVotacaoTemporario objResult = null;
		StringBuilder strHQL = null;
		
		try {

			strHQL = new StringBuilder();
			
			strHQL.append("FROM ViewLocalVotacaoTemporario ")
				  .append("WHERE codObjetoEleitor = :codigoObjetoEleitor ");
	
			objResult = (ViewLocalVotacaoTemporario) getEntityManager().createQuery(strHQL.toString())
																	   .setParameter("codigoObjetoEleitor", id)
																	   .getSingleResult();
		
		} catch (Exception e) {
			
			throw new DBRecuperacaoDadosException(e);
			
		}

		return objResult;
		
	}

}
